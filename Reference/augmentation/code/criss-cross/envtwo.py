
import gym
import numpy as np
class CrissCross(gym.Env):
    def __init__(self, num_servers, num_flows, num_queues, arrival_rates, service_rates, pp,buffer_size):
        super(CrissCross, self).__init__()

        self.num_servers = num_servers
        self.num_flows = num_flows
        self.num_queues = num_queues
        self.arrival_rates = arrival_rates
        self.service_rates = service_rates
        self.buffer_size = buffer_size
        self.pp = pp
        self.queues = np.array([0] * self.num_queues)

        self.action_space = gym.spaces.Discrete(2)
        self.observation_space = gym.spaces.MultiDiscrete([self.buffer_size]*self.num_queues)
        self.t = 0
        self.uniformization_factor = sum(self.arrival_rates) + sum(self.service_rates)
        self.events_probs = [item/self.uniformization_factor for item in self.arrival_rates + self.service_rates]
        self.cumsum_probs = np.cumsum(np.asarray([self.events_probs]))
        self.si_list = [[0,0,0],[1,0,0], [0,0,1], [-1,1,0],[0,-1,0],[0,0,-1]]
        self.server_state = [[1,1],[0,1],[-1,1],[1,-1],[0,-1],[-1,-1]]
        self.phase = [0,0,0]
        self.ss = [-1,-1]
        # x,y x: 0, job 1 1, job 3, y: 1 job 2  -1:no service
        # [0,0,0] fake event

    def reset(self):
        self.queues = np.array([0] * self.num_queues)
        self.phase = [0,0,0]
        return self.queues

    def step(self, action):
        self.t += 1

        if self.queues[0] == 0:
            action = 1
        if self.queues[2] == 0:
            action = 0
        ### make sure that the policy is work-conserving ###
        #ss = [-1,-1]
        si = [0, 0, 0]
        #reward = - np.sum(self.queues)
        xi = np.random.rand()  # generate a random variable
        activity = 0

        assert (~(self.queues[2] == 0 and self.phase[2] == 1))
        while xi > self.cumsum_probs[activity]:
            activity += 1  # activity that will be processed
        ###
        if activity == 0:  # class 1 job arriving
            self.queues = self.queues + [1, 0, 0]
            si = [1, 0 , 0]
        elif activity == 1:  # class 3 job arriving
            self.queues = self.queues + [0, 0, 1]
            si = [0, 0 , 1]
            #sever_state = self.ss
        # class 1 job service completion
        elif activity == 2 and action == 0 and self.queues[0] > 0:  # class 1 job service completion
            self.queues = self.queues + [-1, 1, 0]
            si = [-1, 1 , 0]
        # class 2 job service completion
        elif activity == 3 and self.queues[1] > 0:
            self.queues = self.queues + [0, -1, 0]
            si = [0, -1 , 0]
        # class 3 job service completion
        elif activity == 4 and action == 1 and self.queues[2] > 0:
            if self.phase[2] == 0:
                if np.random.rand() <= self.pp:
                    self.phase[2] = 1
                else:
                    self.queues = self.queues + [0, 0, -1]
            else:
                self.phase[2] = 0
                self.queues = self.queues + [0, 0, -1]
            #self.queues = self.queues + [0, 0, -1]
            si = [0, 0 , -1]
        # else `fake' event; state does not change

        self.queues = self.queues.clip(0,self.buffer_size)
        reward = - np.sum(self.queues)
        done = False
        si_index = self.si_list.index(si)
        return si_index, np.copy(self.phase[2]), np.copy(self.queues), reward, done, {}

    #def step_1(self,state,action):

    def step_1(self,state,phase_,action):
        #p_0 = self.pp/(self.pp+1)
        phase_0 = phase_
        #if np.random.rand() <= p_0:
        #    phase_0 = 1
        #else:
        #    phase_0 = 0
        if state[0] == 0:
            action = 1
        if state[2] == 0:
            action = 0
        ### make sure that the policy is work-conserving ###
        #ss = [-1,-1]
        si = [0, 0, 0]
        #reward = - np.sum(self.queues)
        xi = np.random.rand()  # generate a random variable
        activity = 0

        #assert (~(state[2] == 0 and self.phase[2] == 1))
        while xi > self.cumsum_probs[activity]:
            activity += 1  # activity that will be processed
        ###
        n_state = state
        if activity == 0:  # class 1 job arriving
            n_state = state + [1, 0, 0]
            si = [1, 0 , 0]
        elif activity == 1:  # class 3 job arriving
            n_state = state + [0, 0, 1]
            si = [0, 0 , 1]
            #sever_state = self.ss
        # class 1 job service completion
        elif activity == 2 and action == 0 and state[0] > 0:  # class 1 job service completion
            n_state = state + [-1, 1, 0]
            si = [-1, 1 , 0]
        # class 2 job service completion
        elif activity == 3 and state[1] > 0:
            n_state = state + [0, -1, 0]
            si = [0, -1 , 0]
        # class 3 job service completion
        elif activity == 4 and action == 1 and state[2] > 0:
            if phase_0 == 0:
                if np.random.rand() <= self.pp:
                    phase_0 = 1
                    n_state = state
                else:
                    n_state = state + [0, 0, -1]
            else:
                phase_0 = 0
                n_state = state + [0, 0, -1]
            #self.queues = self.queues + [0, 0, -1]
            si = [0, 0 , -1]
        # else `fake' event; state does not change

        n_state = n_state.clip(0,self.buffer_size)
        reward = - np.sum(n_state)
        done = False
        si_index = self.si_list.index(si)
        #return si_index, np.copy(self.phase[2]), np.copy(n_state), reward, done, {}
        return si_index, phase_0, np.copy(n_state), reward, done, {}

    def close(self):
        pass
