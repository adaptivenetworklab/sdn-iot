"""
Logging and Data Scaling Utilities

Written by Patrick Coady (pat-coady.github.io)
"""
import numpy as np
import sys, os
import shutil
import glob
import csv
import random
import math

def create_log_gaussian(mean, log_std, t):
    quadratic = -((0.5 * (t - mean) / (log_std.exp())).pow(2))
    l = mean.shape
    log_z = log_std
    z = l[-1] * math.log(2 * math.pi)
    log_p = quadratic.sum(dim=-1) - log_z.sum(dim=-1) - 0.5 * z
    return log_p

def logsumexp(inputs, dim=None, keepdim=False):
    if dim is None:
        inputs = inputs.view(-1)
        dim = 0
    s, _ = torch.max(inputs, dim=dim, keepdim=True)
    outputs = s + (inputs - s).exp().sum(dim=dim, keepdim=True).log()
    if not keepdim:
        outputs = outputs.squeeze(dim)
    return outputs

def soft_update(target, source, tau):
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(target_param.data * (1.0 - tau) + param.data * tau)

def hard_update(target, source):
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(param.data)

class Scaler(object):
    """ Generate scale and offset based on running mean and stddev along axis=0

        offset = running mean
        scale = 1 / (stddev + 0.1) / 3 (i.e. 3x stddev = +/- 1.0)
    """

    def __init__(self, obs_dim, initial_states_procedure):
        """
        Args:
            obs_dim: dimension of axis=1
        """
        self.vars = np.zeros(obs_dim)
        self.means = np.zeros(obs_dim)
        self.m = 0
        self.n = 0
        self.first_pass = True
        self.initial_states_procedure = initial_states_procedure
        if  self.initial_states_procedure=='previous_iteration':
            self.initial_states = [np.zeros(obs_dim, 'int32')]
        else:
            self.initial_states = [np.zeros(obs_dim-1, 'int32') for i in range(100)]
    def update_initial(self, x):
        if self.initial_states_procedure == 'previous_iteration':
            self.initial_states = random.sample(list(x), 99)



    def update(self, x):
        """ Update running mean and variance (this is an exact method)
        Args:
            x: NumPy array, shape = (N, obs_dim)

        see: https://stats.stackexchange.com/questions/43159/how-to-calculate-pooled-
               variance-of-two-groups-given-known-group-variances-mean
        """
        #if self.initial_states_procedure == 'previous_iteration':
        #   self.initial_states = random.sample(list(x), 99)

        if self.first_pass:
            self.means = np.mean(x, axis=0)
            self.vars = np.var(x, axis=0)
            self.m = x.shape[0]
            self.first_pass = False
            #self.initial_states = np.random.choice(x, 100)
        else:
            n = x.shape[0]
            new_data_var = np.var(x, axis=0)
            new_data_mean = np.mean(x, axis=0)
            new_data_mean_sq = np.square(new_data_mean)
            new_means = ((self.means * self.m) + (new_data_mean * n)) / (self.m + n)
            self.vars = (((self.m * (self.vars + np.square(self.means))) +
                          (n * (new_data_var + new_data_mean_sq))) / (self.m + n) -
                         np.square(new_means))
            self.vars = np.maximum(0.0, self.vars)  # occasionally goes negative, clip
            self.means = new_means
            self.m += n


    def get(self):
        """ returns 2-tuple: (scale, offset) """
        return 1/(np.sqrt(self.vars) + 0.1)/3, self.means

class ReplayMemory:
    def __init__(self, capacity, seed):
        random.seed(seed)
        self.capacity = capacity
        self.buffer = []
        self.position = 0

    def push(self, state, action, reward, next_state, done):
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = (state, action, reward, next_state, done)
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        state, action, reward, next_state, done = map(np.stack, zip(*batch))
        return state, action, reward, next_state, done

    def push_prob(self, state, action, action_prob, reward, next_state, done):
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = (state, action, action_prob, reward, next_state, done)
        self.position = (self.position + 1) % self.capacity

    def sample_prob(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        state, action, action_prob, reward, next_state, done = map(np.stack, zip(*batch))
        return state, action, action_prob, reward, next_state, done

    def push_queue(self, si, sr, action, reward, next_si, next_sr, done):
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = (si, sr, action, reward, next_si, next_sr, done)
        self.position = (self.position + 1) % self.capacity

    def sample_queue(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        si, sr, action, reward, next_si, next_sr, done = map(np.stack, zip(*batch))
        return si, sr, action, reward, next_si, next_sr, done
        
    def push_two(self, si, sp, sr, action, reward, next_si, next_sp, next_sr, done):
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = (si, sp, sr, action, reward, next_si, next_sp, next_sr, done)
        self.position = (self.position + 1) % self.capacity

    def sample_two(self, batch_size):
        batch = random.sample(self.buffer, batch_size)
        si, sp, sr, action, reward, next_si, next_sp, next_sr, done = map(np.stack, zip(*batch))
        return si, sp, sr, action, reward, next_si, next_sp, next_sr, done

    def sample_trans(self,curr_sr,sample_action,next_srr):
        step = 0
        t = 0
        s = 0
        while s <= 300:
            batch = random.sample(self.buffer,1)
            si, sr, action, reward, next_si, next_sr, done = map(np.stack, zip(*batch))
            if (sr == curr_sr).all() and action == sample_action:
                s += 1
                if (next_sr == next_srr).all():
                    t += 1
            if step >= 1000:
                if s == 0:
                    return 0
                return t/s
                
            step += 1
        return t/s


    def __len__(self):
        return len(self.buffer)

    def sample_mostprev(self,prev_num,batch_size):
        batch = random.sample(self.buffer[self.position-1-prev_num:self.position-1],batch_size)
        si, sr, action, reward, next_si, next_sr, done  = map(np.stack, zip(*batch))
        return si, sr, action, reward, next_si, next_sr, done 

    def sample_mostprev_two(self,prev_num,batch_size):
        batch = random.sample(self.buffer[self.position-1-prev_num:self.position-1],batch_size)
        si, sp, sr, action, reward, next_si, next_sp, next_sr, done = map(np.stack, zip(*batch))
        return si, sp, sr, action, reward, next_si, next_sp, next_sr, done



class Logger(object):
    """ Simple training logger: saves to file and optionally prints to stdout """
    def __init__(self, logname, now, time_start):
        """
        Args:
            logname: name for log (e.g. 'Hopper-v1')
            now: unique sub-directory name (e.g. date/time string)
        """
        self.time_start = time_start
        dirname, _ = os.path.split(os.path.abspath(__file__))
        path = os.path.join(dirname, 'log-files', logname, now)
        os.makedirs(path)
        self.path_weights = os.path.join(path, 'weights')
        os.makedirs(self.path_weights)
        filenames = glob.glob('*.py')  # put copy of all python files in log_dir
        for filename in filenames:     # for reference
            shutil.copy(filename, path)

        path = os.path.join(path, 'log.csv')

        self.write_header = True
        self.log_entry = {}
        self.f = open(path, 'w')
        self.writer = None  # DictWriter created with first call to write() method





    def write(self, display=True):
        """ Write 1 log entry to file, and optionally to stdout
        Log fields preceded by '_' will not be printed to stdout

        Args:
            display: boolean, print to stdout
        """
        if display:
            self.disp(self.log_entry)
        if self.write_header:
            fieldnames = [x for x in self.log_entry.keys()]
            self.writer = csv.DictWriter(self.f, fieldnames=fieldnames)
            self.writer.writeheader()
            self.write_header = False
        self.writer.writerow(self.log_entry)
        self.log_entry = {}

    @staticmethod
    def disp(log):
        """Print metrics to stdout"""
        log_keys = [k for k in log.keys()]
        log_keys.sort()
        print('***** Episode {}, Average Cost = {:.1f} *****'.format(log['_Episode'],
                                                               log['_AverageReward']))
        for key in log_keys:
            if key[0] != '_':  # don't display log items with leading '_'
                print('{:s}: {:.3g}'.format(key, log[key]))
        print('\n')

    def log(self, items):
        """ Update fields in log (does not write to file, used to collect updates.

        Args:
            items: dictionary of items to update
        """
        self.log_entry.update(items)

    def close(self):
        """ Close log file - log cannot be written after this """
        self.f.close()
