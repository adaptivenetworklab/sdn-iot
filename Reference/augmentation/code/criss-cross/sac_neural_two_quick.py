import os
import torch
import torch.nn.functional as F
from torch.optim import Adam
import numpy as np
from utils import soft_update, hard_update
from model import GaussianPolicy, QNetwork, DeterministicPolicy , GaussianPolicy_discrete
from model import DQNNET
from aprox_sd_two import Stationary
import matplotlib.pyplot as plt
from scipy import special

class SAC_neural(object):
    def __init__(self, num_inputssi, num_inputssp, num_inputssr, action_space, args):

        self.gamma = args.gamma
        self.tau = args.tau
        self.alpha = args.alpha
        self.pp = 0.8
        self.arrival_rates = [args.arrival, args.arrival]
        self.service_rates = [2.0, args.service, 2.0]
        self.uniformization_factor = sum(self.arrival_rates) + sum(self.service_rates)
        self.events_probs = [item/self.uniformization_factor for item in self.arrival_rates + self.service_rates]
        self.cumsum_probs = np.cumsum(np.asarray([self.events_probs]))

        self.policy_type = args.policy
        self.target_update_interval = args.target_update_interval
        self.automatic_entropy_tuning = args.automatic_entropy_tuning
        self.args = args

        self.device = torch.device("cuda" if args.cuda else "cpu")

        #self.critic = QNetwork(num_inputssi + num_inputssp + num_inputssr, action_space.n, args.hidden_size).to(device=self.device)
        self.critic = DQNNET(num_inputssi + num_inputssp + num_inputssr, action_space.n, args.hidden_size).to(device=self.device)
        self.critic_optim = Adam(self.critic.parameters(), lr=args.lr)
        self.critic_target = DQNNET(num_inputssi + num_inputssp + num_inputssr, action_space.n, args.hidden_size).to(self.device)
        hard_update(self.critic_target, self.critic)

        if self.policy_type == "Gaussian":
            # Target Entropy = −dim(A) (e.g. , -6 for HalfCheetah-v2) as given in the paper
            if self.automatic_entropy_tuning is True:
                self.target_entropy = -torch.prod(torch.Tensor(action_space.n).to(self.device)).item()
                self.log_alpha = torch.zeros(1, requires_grad=True, device=self.device)
                self.alpha_optim = Adam([self.log_alpha], lr=args.lr)

            self.policy = GaussianPolicy_discrete(num_inputssi + num_inputssp + num_inputssr, action_space.n, args.hidden_size).to(self.device)
            #self.policy = GaussianPolicy(num_inputs, action_space.n, args.hidden_size)
            self.policy_optim = Adam(self.policy.parameters(), lr=args.lr)

        else:
            self.alpha = 0
            self.automatic_entropy_tuning = False
            self.policy = DeterministicPolicy(num_inputssr, action_space.n, args.hidden_size)
            self.policy_optim = Adam(self.policy.parameters(), lr=args.lr)
        self.state_list = np.array([]).reshape(0,3)
        self.sd = np.array([])
        self.tabular_dis = np.array([])
        self.net_ratio = np.array([])
        self.mlen = int(args.buffer_size) +1
    def state_to_index(self,state):
        dim = int(self.mlen)
        index = int(state[0]) * int(dim**2) + int(state[1])* int(dim) + int(state[2])
        return int(index)

    def select_action(self, si, sp, sr, evaluate=False):
        if sr[0] == 0:
            return 1
        if sr[2] == 0:
            return 0
        si_tensor = torch.tensor(si).to(self.device)
        si_onehot = F.one_hot(si_tensor, num_classes = 6)

        sp_tensor = torch.tensor(sp).to(self.device)
        sp_onehot = F.one_hot(sp_tensor, num_classes = 2)

        state_sr = torch.FloatTensor(sr).to(self.device)

        state = torch.cat([si_onehot,sp_onehot,state_sr],0).to(self.device).unsqueeze(0)
        action = self.critic(state).data.max(1)[1].detach().cpu().numpy()

        '''
        if evaluate is False:
            action, _, _ = self.policy.sample(state)
        else:
            with torch.no_grad():
                _, z, action = self.policy.sample(state)
        action = action.detach().cpu().numpy()
        '''
        return action[0]


    def initialize_aprox_net(self,memory):
        self.aprox_SD.normalize(memory)

    def update_parameters(self, memory, memory_u, batch_size, scaler, args, updates, sd_updates,i_episode):
        # Sample a batch from memory
        #si_batch, sr_batch, action_batch, reward_batch, next_si_batch, next_sr_batch, mask_batch = memory.sample_queue(batch_size=batch_size)
        if len(memory) < batch_size:
            return
        __si_batch, __sp_batch, __sr_batch, __action_batch, __reward_batch, __next_si_batch, __next_sp_batch, __next_sr_batch, __mask_batch = memory.sample_two(batch_size=batch_size)
        scale, offset = scaler.get()

        zero_ind = np.any(__sr_batch==0,axis=1)
        #zero_ind = np.any(__sr_batch[:,0].reshape(batch_size,1)==0,axis=1) ^ np.any(__sr_batch[:,2].reshape(batch_size,1)==0,axis=1)
        si_batch = __si_batch[~zero_ind]

        sp_batch = __sp_batch[~zero_ind]
        sr_batch = __sr_batch[~zero_ind]
        action_batch = __action_batch[~zero_ind]
        reward_batch = __reward_batch[~zero_ind]
        next_si_batch = __next_si_batch[~zero_ind]
        next_sp_batch = __next_sp_batch[~zero_ind]
        next_sr_batch = __next_sr_batch[~zero_ind]
        mask_batch = __mask_batch[~zero_ind]
        batch_size_ = si_batch.shape[0]

        if batch_size_ == 0 or not args.virtual:
            scaled_sr = (__sr_batch - offset) * scale
            next_scaled_sr = (__next_sr_batch - offset) * scale
            si_batch = torch.LongTensor(__si_batch).to(self.device)
            sp_batch = torch.LongTensor(__sp_batch).to(self.device)
            scaled_sr_batch = torch.FloatTensor(scaled_sr).to(self.device)

            next_si_batch = torch.LongTensor(__next_si_batch).to(self.device)
            next_sp_batch = torch.LongTensor(__next_sp_batch).to(self.device)
            scaled_next_sr_batch = torch.FloatTensor(next_scaled_sr).to(self.device)

            action_batch_r = torch.LongTensor(__action_batch).to(self.device).unsqueeze(1)
            reward_batch_r = torch.FloatTensor(__reward_batch).to(self.device).unsqueeze(1)

            si_onehot = F.one_hot(si_batch, num_classes = 6)
            sp_onehot = F.one_hot(sp_batch, num_classes = 2)
            next_si_onehot = F.one_hot(next_si_batch, num_classes = 6)
            next_sp_onehot = F.one_hot(next_sp_batch, num_classes = 2)
        else:
            si_batch_ = np.repeat(si_batch,args.batch_size_v - 1, axis=0) #repeat 123123
            sp_batch_ = np.repeat(sp_batch,args.batch_size_v - 1, axis=0) #repeat 123123
            sr_batch_ = np.repeat(sr_batch,args.batch_size_v - 1, axis=0) #repeat 123123

            next_sr_batch_ = np.repeat(next_sr_batch,args.batch_size_v - 1, axis=0) #repeat 123123
            change_batch_ = next_sr_batch_ - sr_batch_

            if args.uniform:
                virtual_sr_= np.random.uniform(low = 0.0,high = self.mlen - 1,size = (3,args.batch_size_v - 1) ).clip(0, self.mlen -1)
                virtual_sr_ = np.transpose(virtual_sr_).astype(int).clip(0,self.mlen -1)
            else:
                virtual_sr_= [np.random.normal(offset[n], 1. / scale[n], batch_size_ * (args.batch_size_v - 1)).clip(1, self.mlen -1) for n in np.arange(3)]
                virtual_sr_ = np.transpose(virtual_sr_).astype(int).clip(1,self.mlen -1)

            virtual_sr_batch = np.vstack([__sr_batch, virtual_sr_])
            next_virtual_sr_ = (virtual_sr_ + change_batch_).clip(0,args.buffer_size)
            virtual_next_sr_batch = np.vstack([__next_sr_batch, next_virtual_sr_])

            virtual_reward_ = np.array(-np.sum(next_virtual_sr_,axis=1)).reshape(next_virtual_sr_.shape[0],1)

            __reward_batch = __reward_batch.reshape(batch_size,1)
            virtual_reward_batch = np.vstack([__reward_batch, virtual_reward_])

            __action_batch = __action_batch.reshape(batch_size,1)
            action_batch = action_batch.reshape(batch_size_,1)
            virtual_action_ = np.repeat(action_batch,args.batch_size_v - 1,axis=0).reshape(batch_size_ * (args.batch_size_v - 1),1)
            virtual_action_batch = np.vstack([__action_batch, virtual_action_])

            si_batch_ = np.vstack([__si_batch.reshape(batch_size,1), si_batch_.reshape(si_batch_.shape[0],1)])
            sp_batch_ = np.vstack([__sp_batch.reshape(batch_size,1), sp_batch_.reshape(sp_batch_.shape[0],1)])

            next_si_batch_ = np.repeat(next_si_batch,args.batch_size_v - 1, axis=0) #repeat 123123
            next_sp_batch_ = np.repeat(next_sp_batch,args.batch_size_v - 1, axis=0) #repeat 123123
            next_si_batch_ = np.vstack([__next_si_batch.reshape(batch_size,1), next_si_batch_.reshape(next_si_batch_.shape[0],1)])
            next_sp_batch_ = np.vstack([__next_sp_batch.reshape(batch_size,1), next_sp_batch_.reshape(next_sp_batch_.shape[0],1)])

            si_batch_ = np.squeeze(si_batch_)
            sp_batch_ = np.squeeze(sp_batch_)
            next_si_batch_ = np.squeeze(next_si_batch_)
            next_sp_batch_ = np.squeeze(next_sp_batch_)

            scaled_sr = (virtual_sr_batch - offset) * scale
            next_scaled_sr = (virtual_next_sr_batch - offset) * scale

            si_batch_r = torch.LongTensor(si_batch_).to(self.device)
            sp_batch_r = torch.LongTensor(sp_batch_).to(self.device)
            scaled_sr_batch = torch.FloatTensor(scaled_sr).to(self.device)

            next_si_batch_r = torch.LongTensor(next_si_batch_).to(self.device)
            next_sp_batch_r = torch.LongTensor(next_sp_batch_).to(self.device)
            scaled_next_sr_batch = torch.FloatTensor(next_scaled_sr).to(self.device)

            action_batch_r = torch.LongTensor(virtual_action_batch).to(self.device)
            reward_batch_r = torch.FloatTensor(virtual_reward_batch).to(self.device)

            si_onehot = F.one_hot(si_batch_r, num_classes = 6)
            sp_onehot = F.one_hot(sp_batch_r, num_classes = 2)
            next_si_onehot = F.one_hot(next_si_batch_r, num_classes = 6)
            next_sp_onehot = F.one_hot(next_sp_batch_r, num_classes = 2)

        state_batch = torch.cat([si_onehot, sp_onehot, scaled_sr_batch], 1).to(self.device)
        next_state_batch = torch.cat([next_si_onehot, next_sp_onehot, scaled_next_sr_batch] , 1).to(self.device)

        with torch.no_grad():
            target_Q = self.critic_target(next_state_batch).detach().max(1)[0]
            #next_state_action, (action_probabilities, log_action_probabilities), _ = self.policy.sample(next_state_batch)
            #qf1_next_target, qf2_next_target = self.critic_target(next_state_batch)
            #min_qf_next_target = action_probabilities * (torch.min(qf1_next_target, qf2_next_target) - self.alpha * log_action_probabilities)
            #min_qf_next_target = min_qf_next_target.sum(dim=1).unsqueeze(-1)
            target_Q = target_Q.unsqueeze(-1)
            next_q_value = reward_batch_r + self.gamma * (target_Q)
        qf = self.critic(state_batch)
        qf = qf.gather(1,action_batch_r)  # Two Q-functions to mitigate positive bias in the policy improvement step
        #qf2 = qf2.gather(1,action_batch_r)  # Two Q-functions to mitigate positive bias in the policy improvement step
        qf_loss = F.mse_loss(qf, next_q_value)  # JQ = 𝔼(st,at)~D[0.5(Q1(st,at) - r(st,at) - γ(𝔼st+1~p[V(st+1)]))^2]
        #qf2_loss = F.mse_loss(qf2, next_q_value)  # JQ = 𝔼(st,at)~D[0.5(Q1(st,at) - r(st,at) - γ(𝔼st+1~p[V(st+1)]))^2]
        #qf_loss = qf1_loss + qf2_loss
        self.critic_optim.zero_grad()
        qf_loss.backward()
        self.critic_optim.step()

        #train policy
        #action, (action_probabilities, log_action_probabilities), _ = self.policy.sample(state_batch)
        #qf1_pi, qf2_pi = self.critic(state_batch)
        #min_qf_pi = torch.min(qf1_pi, qf2_pi)
        #inside_term = self.alpha * log_action_probabilities - min_qf_pi
        #policy_loss = (action_probabilities * inside_term).sum(dim=1).mean()
        #log_pi = torch.sum(log_action_probabilities * action_probabilities, dim=1)

        '''
        pi, log_pi, _ = self.policy.sample(state_batch)
        qf1_pi, qf2_pi = self.critic(state_batch, pi)
        min_qf_pi = torch.min(qf1_pi, qf2_pi)
        policy_loss = ((self.alpha * log_pi) - min_qf_pi).mean() # Jπ = 𝔼st∼D,εt∼N[α * logπ(f(εt;st)|st) − Q(st,f(εt;st))]
        '''
        '''
        self.policy_optim.zero_grad()
        policy_loss.backward()
        self.policy_optim.step()
        if self.automatic_entropy_tuning:
            alpha_loss = -(self.log_alpha * (log_pi + self.target_entropy).detach()).mean()
            self.alpha_optim.zero_grad()
            alpha_loss.backward()
            self.alpha_optim.step()
            self.alpha = self.log_alpha.exp()
            alpha_tlogs = self.alpha.clone() # For TensorboardX logs
        else:
            alpha_loss = torch.tensor(0.).to(self.device)
            alpha_tlogs = torch.tensor(self.alpha) # For TensorboardX logs
        if updates % self.target_update_interval == 0:
            soft_update(self.critic_target, self.critic, self.tau)
        '''
        return qf_loss.item()

    # Save model parameters
    def save_model(self, env_name, suffix="", actor_path=None, critic_path=None):
        if not os.path.exists('models/'):
            os.makedirs('models/')

        if actor_path is None:
            actor_path = "models/sac_actor_{}_{}".format(env_name, suffix)
        if critic_path is None:
            critic_path = "models/sac_critic_{}_{}".format(env_name, suffix)
        print('Saving models to {} and {}'.format(actor_path, critic_path))
        torch.save(self.policy.state_dict(), actor_path)
        torch.save(self.critic.state_dict(), critic_path)

    # Load model parameters
    def load_model(self, actor_path, critic_path):
        print('Loading models from {} and {}'.format(actor_path, critic_path))
        if actor_path is not None:
            self.policy.load_state_dict(torch.load(actor_path))
        if critic_path is not None:
            self.critic.load_state_dict(torch.load(critic_path))
