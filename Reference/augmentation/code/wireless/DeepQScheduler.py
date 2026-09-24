#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import os
import pandas as pd
import argparse
import torch
import torch.nn as nn
import torch.optim as optim
import time
import numpy as np
import matplotlib.pyplot as plt
from wireless_env import WirelessEnv
from utils import soft_update, hard_update
from model import GaussianPolicy, QNetwork, DeterministicPolicy , GaussianPolicy_discrete
from utils import Scaler
from utils import ReplayMemory
from sac_neural_quick_2 import SAC_neural
from utils import hard_update

def maxWeightScheduler(state, Capacity):
    return np.argmax(state*Capacity)

def test(timeslotsTest, scaler, scaler_a, scaler_v, agent, policy, show=False):
    #policy = "Max-Weight"
    test_env = WirelessEnv(Channels, Arrivals, Capacity, buffer=1000)
    stateTracker_ = np.zeros([Channels, timeslotsTest])
    arrival_, state_, service_ = test_env.reset()

    MeanQlength = 0.0
    for t in range(timeslotsTest):
        stateTracker_[:, t] = state_
        t_scale, t_offset = scaler.get()
        t_scale_a, t_offset_a = scaler_a.get()
        t_scale_v, t_offset_v = scaler_v.get()

        t_observes = (state_ - t_offset) * t_scale
        t_observes_a = (arrival_ - t_offset_a) * t_scale_a
        t_observes_v = (service_ - t_offset_v) * t_scale_v

        if policy == "Max-Weight":
            test_action = maxWeightScheduler(state_, service_)
        else:
            test_action = agent.select_action(t_observes_a, t_observes, t_observes_v)  # Sample action from policy

        arrival_, state_, service_, reward_,  is_done = test_env.step(test_action)

        MeanQlength = MeanQlength * t * 1.0 / (t + 1) + sum(state_) * 1.0 / (t + 1)
    print(f"{policy} || mean queue length is", round(MeanQlength, 3))

    if show:
        plt.figure(0)
        x = np.array(range(timeslotsTest))
        plt.plot(x, stateTracker_[0, :], x, stateTracker_[1, :], x, stateTracker_[2, :])
        plt.legend(('Queue 0', 'Queue 1', 'Queue 2'), loc='best')
        plt.xlabel('time')
        plt.ylabel('Queue length')
        if policy == "Max-Weight":
            plt.title("Max-Weight: " + "mean queue length=" + str(round(MeanQlength, 3)))
        else:
            plt.title("Learned Scheduler: " + "mean queue length=" + str(round(MeanQlength, 3)))
        plt.show()
    return round(MeanQlength, 3)


parser = argparse.ArgumentParser(description=('Train policy for a queueing network'))
parser.add_argument('--env-name', default="queuing_rl")
parser.add_argument('-g', '--gamma', type=float, help='Discount factor',
                        default = 0.99)
parser.add_argument('--batch_size', type=int, help='Number of episodes per training batch',
                        default = 256)
parser.add_argument('--batch_size_v', type=int, help='Number of episodes per training batch',
                        default = 100)
parser.add_argument('--virtual_loop', type=int, help='Number of virtual batch_size',
                        default = 10)
parser.add_argument('-m', '--hidden_size', type=int, help='Size of first hidden layer for value and policy NNs',
                        default = 128)
parser.add_argument('--buffer_size', type=int, help='Size of buffer size',
                        default = 100)
parser.add_argument('--sample_size', type=int, help='Size of buffer size',
                        default = 50)
parser.add_argument('-t', '--total_steps', type=int, help='Number of total time-steps',
                        default = 2000000)
parser.add_argument('--update_frequence', type=int, help='frequency of updating networks',
                        default = 500)
parser.add_argument('--test_frequence', type=int, help='frequency of testing',
                        default = 3000)
parser.add_argument('-check','--check', action='store_true', help='whether sanity check')
parser.add_argument('-s', '--seed', type=int, help='random seed',
                        default = 1234)
parser.add_argument("--log_dir", default="temp_neural_2")
parser.add_argument('--tau', type=float, default=0.005, metavar='G',
                    help='target smoothing coefficient(τ) (default: 0.005)')
parser.add_argument('--epsilon', type=float, default=1, metavar='G')
parser.add_argument('--arrival', type=float, default=0.9, metavar='G')
parser.add_argument('--lr', type=float, default=0.0003, metavar='G',
                    help='learning rate (default: 0.0003)')
parser.add_argument('--alpha', type=float, default=0.2, metavar='G',
                    help='Temperature parameter α determines the relative importance of the entropy\
                            term against the reward (default: 0.2)')
parser.add_argument('--automatic_entropy_tuning', type=bool, default=True, metavar='G',
                    help='Automaically adjust α (default: False)')
parser.add_argument('--cuda', action="store_true",
                    help='run on CUDA (default: False)')
parser.add_argument('--virtual', action="store_true",
                    help='use virtual queues')
parser.add_argument('--distributed', action="store_true",
                    help='use distributed-virtual queues')
parser.add_argument('--uniform', action="store_true",
                    help='use uniform distributed-virtual queues')
parser.add_argument('--policy', default="Gaussian",
                    help='Policy Type: Gaussian | Deterministic (default: Gaussian)')
parser.add_argument('--target_update_interval', type=int, default=1, metavar='N',
                    help='Value target update per no. of updates per step (default: 1)')
parser.add_argument('--start_steps', type=int, default=1000, metavar='N',
                    help='Steps sampling random actions (default: 10000)')
parser.add_argument('--u_num', type=int, help='number of uniformly distributed samples',
                    default =240000)

args = parser.parse_args()




if __name__ == '__main__':
    Channels = 3
    Arrivals = [2, 4, 3]
    Capacity = [12, 12, 12]
    env = WirelessEnv(Channels, Arrivals, Capacity, buffer = args.buffer_size)
    env_dis = WirelessEnv(Channels, Arrivals, Capacity, buffer = 200)

    episodes = 1
    timeslots = 100000
    WATCH_PERIOD = timeslots//100
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(device)
    print(args.seed)
    file_name = f"seed_{args.seed}"
    if not os.path.exists(
        f'./{args.log_dir}/{file_name}'):
        os.makedirs(
        f'./{args.log_dir}/{file_name}')
    scaler = Scaler(Channels,initial_states_procedure = "empty")
    xxx = np.zeros((100000, Channels), dtype= 'int8')
    scaler.update_initial(xxx)

    scaler_a = Scaler(Channels,initial_states_procedure = "empty")
    xxx_a = np.zeros((100000, Channels), dtype= 'int8')
    scaler_a.update_initial(xxx_a)

    scaler_v = Scaler(Channels,initial_states_procedure = "empty")
    xxx_v = np.zeros((100000, Channels), dtype= 'int8')
    scaler_v.update_initial(xxx_v)


    agent = SAC_neural(Channels , Channels, args)
    memory = ReplayMemory(args.total_steps, args.seed)
    timeslotsTest = int(2e5)
    #test(timeslotsTest, scaler, scaler_a, scaler_v, agent, "Max-Weight")

    if not os.path.exists(f'./{args.log_dir}'):
        os.makedirs(f'./{args.log_dir}')

    total_episodes = int(args.total_steps /  args.update_frequence)

    total_reward = []
    queue_list = []
    arrival, state, service = env.reset()
    total_numsteps = 0
    test_rewards = []
    mmm = 0

    #for episode in range(episodes):
    for episode in range(total_episodes):
        stime = time.time()
        episode_reward = []
        episode_steps = 0
        for step_ in range(args.update_frequence):
        #for timeslot in range(timeslots):
            if np.random.rand() < args.epsilon:
                action = int(np.random.choice(Channels))
            else:
                scale, offset = scaler.get()
                observes = (state - offset) * scale

                scale_a, offset_a = scaler_a.get()
                observes_a = (arrival - offset_a) * scale_a

                scale_v, offset_v = scaler_v.get()
                observes_v = (service - offset_v) * scale_v

                action = agent.select_action(observes_a, observes, observes_v)  # Sample action from policy
            next_arrival, next_state, next_service, reward, is_done = env.step(action)

            scaler.update(np.array([next_state]))
            scaler_a.update(np.array([next_arrival]))
            scaler_v.update(np.array([next_service]))

            memory.push_two(arrival, state, service, action, reward, next_arrival, next_state, next_service, 1) # Append transition to memory

            episode_reward.append(reward)
            total_reward.append(reward)
            queue_list.append(np.sum(next_state))
            episode_steps += 1
            total_numsteps += 1

            state = next_state
            arrival = next_arrival
            service = next_service
            if args.epsilon >= 0.01:
                args.epsilon = args.epsilon * 0.99


        if args.start_steps < total_numsteps:
            memory_u = memory
            for tt in range(500):
                for ss_ in range(args.virtual_loop):
                    #agent.update_parameters(memory, memory_u, args.batch_size, scaler, args, ss_, tt, i_episode)
                    agent.update_parameters(memory, memory_u, args.batch_size, scaler, scaler_a, scaler_v, args, ss_, tt, Capacity)
                if tt % 10 == 0:
                    hard_update(agent.critic_target, agent.critic)
        print("running time per eps is ", time.time() - stime)
        print(f"Episode: {episode}, total numsteps: {total_numsteps}, Episode: average_reward: {np.mean(episode_reward,axis=0)}, total_average_reward: {np.mean(total_reward,axis=0)}, average_queue_length: {np.mean(queue_list)} epsilon: {args.epsilon}")
        test_rewards.append(np.mean(queue_list[-100000:]))

        if (episode+1) % 5 == 0:
            data = np.array(test_rewards)
            df = pd.DataFrame(data=data,columns=["Average Queue"]).reset_index()
            df.to_csv(f'./{args.log_dir}/progress_{args.virtual}_seed{args.seed}_train_u_{args.uniform}.csv', index = False)
        if episode >= 50:
            if test_rewards[-1] <= 10.5:
                break

        if (episode) % 20 == 0:
            testq = test(timeslotsTest, scaler, scaler_a, scaler_v, agent, "sac", show=False)
            results = [episode, total_numsteps, testq, np.mean(queue_list[-100000:])]
            df = pd.DataFrame(data=[results],
                              columns=["i_episode", "total_numsteps", "avg_test_reward", "avg_traing_queuue_length"])
            if not os.path.exists(
                    f'./{args.log_dir}/{file_name}/progress_test.csv'):
                df.to_csv(
                    f'./{args.log_dir}/{file_name}/progress_test.csv',index=False)
            else:
                df.to_csv(
                    f'./{args.log_dir}/{file_name}/progress_test.csv',index=False, mode='a', header=False)

    data = np.array(test_rewards)
    df = pd.DataFrame(data=data,columns=["Average QUEUE"]).reset_index()
    df.to_csv(f'./{args.log_dir}/progress_{args.virtual}_seed{args.seed}_train_u_{args.uniform}.csv', index = False)
