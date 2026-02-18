import numpy as np
import gym
from scipy.stats import poisson
from scipy.stats import gamma

class WirelessEnv(gym.Env):
    def __init__(self, Channels, Arrivals, Capacity, buffer):
        self.Channels = Channels
        self.Arrivals = Arrivals
        self.Capacity = Capacity
        self.buffer = buffer

        self.action_space = Channels
        self.observation_space = Channels

        self.reset()

    def step(self, action):
        state = self.state
        if int(state[action]) == 0:
            zeros = np.where(state != 0)[0]
            if len(zeros) >= 1:
                action = np.random.choice(zeros,1)[0]
        # Arrival and departure
        # arrival was known beforehand
        #arrival = poisson.rvs(self.Arrivals, size = self.Channels)
        service = np.zeros(self.Channels)
        #service_a = poisson.rvs(self.Capacity[action], size = 1)
        #service[action] = service_a
        #service[action] = self.Capacity[action]
        service[action] = self.service[action]
        # state update
        state = np.clip(state + self.arrival - service, a_min=0, a_max=self.buffer)
        done = False
        #reward = -sum(state)/max(self.Capacity)**2
        #reward = -sum(state)/max(self.Capacity)**2
        #reward = (3 * self.buffer - sum(state)) / (3 * self.buffer)
        reward = -sum(state)/20
        reward = max(reward,-30.0)
        #reward = -sum(state)
        #reward = max(reward, -100.0)
        self.state = state
        self.arrival = poisson.rvs(self.Arrivals, size = self.Channels)
        self.service = gamma.rvs(self.Capacity, size = self.Channels)
        return  np.copy(np.array(self.arrival, dtype = np.float32)), np.copy(np.array(self.state, dtype = np.float32)), \
                np.copy(np.array(self.service, dtype = np.float32)), np.array(reward, dtype=np.float32),  done


    def reset(self):
        self.state = np.random.randint(10, size=self.Channels) + 1
        self.arrival = poisson.rvs(self.Arrivals, size = self.Channels)
        #self.service = poisson.rvs(self.Capacity, size = self.Channels)
        self.service = gamma.rvs(self.Capacity, size = self.Channels)
        return np.array(self.arrival, dtype = np.float32), np.array(self.state, dtype = np.float32), np.array(self.service, dtype = np.float32)

"""
Channels = 3
Arrivals = [2,3,4]
Capacity = [3,4,5]
WirelessChannel = WirelessEnv(Channels, Arrivals, Capacity)

arrival_sum = np.zeros((1,3), dtype='float')
service_sum = np.zeros((1,3), dtype='float')

timeslots = 1000
for i in range(timeslots):
    state, reward, arrival, service, done = WirelessChannel.step(np.random.choice(Channels))
    arrival_sum += arrival
    service_sum += service

arrival_ave = arrival_sum/timeslots
service_ave = service_sum/timeslots
"""
