import gym
import numpy as np
import argparse
from sac_neural_two_quick import SAC_neural
from gym import spaces
from envtwo import CrissCross
import datetime
import itertools
from utils import hard_update
from torch.utils.tensorboard import SummaryWriter
import pandas as pd
from utils import ReplayMemory
import sys
from utils import Scaler
import time

def test_policy(agent,scaler,sr,ar):
    num_servers, num_flows, num_queues = 2, 2, 3
    arrival_rates = ar
    service_rates = sr
    pp = 0.8
    test_env = CrissCross(num_servers, num_flows, num_queues, arrival_rates, service_rates, pp, buffer_size=20)
    rewards_record = []
    B1, B2, B3 = [], [], []
    test_sr = test_env.reset()
    test_sp = 0
    test_si = 0
    total_events = 3*10**6
    for tt in range(total_events):
        t_scale, t_offset = scaler.get()
        t_observes = (test_sr - t_offset) * t_scale
        test_action = agent.select_action(test_si, test_sp, t_observes, evaluate = True)  # Sample action from policy
        if test_sr[0] == 0:
            test_action = 1
        elif test_sr[2] == 0:
            test_action = 0
        ntest_si, ntest_sp, ntest_sr, test_r, test_done, test_info = test_env.step(test_action)
        rewards_record.append(test_r)
        B1 += [ntest_sr[0]]
        B2 += [ntest_sr[1]]
        B3 += [ntest_sr[2]]
        test_si = ntest_si
        test_sr = ntest_sr
        test_sp = ntest_sp

    print(f"Total AQL of agetn policy sim is {-sum(rewards_record)/total_events}")
    print(f"AQL B1 of agent policy sim is {sum(B1)/total_events}")
    print(f"AQL B2 of agent policy sim is {sum(B2)/total_events}")
    print(f"AQL B3 of agent policy sim is {sum(B3)/total_events}")
    print(f"======================================================================")
    return (-sum(rewards_record)/total_events), (sum(B1)/total_events), (sum(B2)/total_events) ,(sum(B3)/total_events)

def main(args):
    num_servers, num_flows, num_queues = 2, 2, 3
    load = 0.6
    pp = 0.8
    arrival_rates = [args.arrival, args.arrival]
    service_rates = [2.0, args.service, 2.0]
    env = CrissCross(num_servers, num_flows, num_queues, arrival_rates, service_rates, pp,buffer_size=args.buffer_size)
    env_dis = CrissCross(num_servers, num_flows, num_queues, arrival_rates, service_rates, pp,buffer_size=args.buffer_size)
    env.seed(args.seed)
    total_events = args.total_steps

    if args.check:
        start_time = datetime.datetime.now()
        print("==========begin snaity check===========")
        rewards_record = []
        B1, B2, B3 = [], [], []

        # random policy
        obs = env.reset()
        for it in range(total_events):
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            rewards_record.append(reward)
            B1 += [obs[0]]
            B2 += [obs[1]]
            B3 += [obs[2]]
        print(f"AQL B1 of random policy theory is {load/(2.0-2.0*load)}")
        print(f"AQL B2 of random policy theory is {load/(1.0-load)}")
        print(f"AQL B3 of random policy theory is {load/(2.0-2.0*load)}")
        print(f"Total AQL of random policy sim is {-sum(rewards_record)/total_events}")
        print(f"AQL B1 of random policy sim is {sum(B1)/total_events}")
        print(f"AQL B2 of random policy sim is {sum(B2)/total_events}")
        print(f"AQL B3 of random policy sim is {sum(B3)/total_events}")
        print(f"======================================================================")

        # priority policy
        rewards_record = []
        B1, B2, B3 = [], [], []
        obs = env.reset()
        for it in range(total_events):
            if obs[0] > 0:
                action = 0
            else:
                action = 1
            obs, reward, done, info = env.step(action)
            rewards_record.append(reward)
            B1 += [obs[0]]
            B2 += [obs[1]]
            B3 += [obs[2]]

        print(f"AQL B1 of priority policy theory is {load/(2.0-load)}")
        print(f"AQL B2 of priority policy theory is {load/(1.0-load)}")
        print(f"AQL B3 of priority policy theory is {2*load/(2.0-2.0*load)-load/(2.0-load)}")
        print(f"Total AQL of priority policy sim is {-sum(rewards_record)/total_events}")
        print(f"AQL B1 of priority policy sim is {np.mean(B1)}")
        print(f"AQL B2 of priority policy sim is {np.mean(B2)}")
        print(f"AQL B3 of priority policy sim is {np.mean(B3)}")

        end_time = datetime.datetime.now()
        time_check = end_time - start_time
        print('time of snaity eheck:', int((time_check.total_seconds() / 60) * 100) / 100., 'minutes')

    print("==========begin RL tasks===========")
    start_time = datetime.datetime.now()
    print(f"observation_si_space: {len(env.si_list) + env.observation_space.shape[0]}, observation_sr_length: {args.buffer_size}, action_space: {env.action_space.n}")
    # Agent
    #agent = SAC(env.observation_space.shape[0], env.action_space, args)
    agent = SAC_neural(len(env.si_list), 2, env.observation_space.shape[0], env.action_space, args)
    # Memory
    memory = ReplayMemory(args.total_steps, args.seed)
    # Training Loop
    total_numsteps = 0
    updates = 0
    total_episodes = int(args.total_steps /  args.update_frequence)
    total_reward = []
    queue_list = []
    file_name = f"seed_{args.seed}"
    state_sr = env.reset()
    state_si = 0
    state_sp = 0
    show_int = 0
    #event state, phase state
    scaler = Scaler(len(service_rates),initial_states_procedure = "empty")
    xxx = np.zeros((200000, env.observation_space.shape[0]), dtype= 'int8')
    scaler.update_initial(xxx)
    test_rewards = []
    for i_episode in range(total_episodes):
        episode_reward = []
        episode_steps = 0
        for step_ in range(args.update_frequence):
            if np.random.rand() < args.epsilon:
                if state_sr[0] > 0:
                    action = 0
                else:
                    action = 1
            else:
                scale, offset = scaler.get()
                observes = (state_sr - offset) * scale
                action = agent.select_action(state_si, state_sp, observes)  # Sample action from policy

            next_state_si, next_state_sp, next_state_sr, reward, done, info = env.step(action)
            scaler.update(np.array([next_state_sr]))

            queue_list.append(-reward)
            episode_reward.append(next_state_sr)
            total_reward.append(next_state_sr)

            episode_steps += 1
            total_numsteps += 1

            memory.push_two(state_si, state_sp, state_sr, action, reward, next_state_si, next_state_sp, next_state_sr, 1) # Append transition to memory

            state_si = next_state_si
            state_sp = next_state_sp
            state_sr = next_state_sr

            if args.epsilon >= 0.01:
                args.epsilon = args.epsilon * 0.90
        if args.start_steps < total_numsteps:
            memory_u = memory
            for tt in range(500):
                for ss_ in range(args.virtual_loop):
                    agent.update_parameters(memory, memory_u,args.batch_size, scaler, args, ss_, tt, i_episode)
                if tt % 10 == 0:
                    hard_update(agent.critic_target, agent.critic)
        print(f"Episode: {i_episode}, total numsteps: {total_numsteps}, Episode: average_reward: {np.mean(episode_reward,axis=0)}, total_average_reward: {np.mean(total_reward,axis=0)}, average_queue_length: {np.mean(np.array(queue_list)[-200000:])}, epsilon: {args.epsilon}")
        end_time = datetime.datetime.now()
        print(f"Time consuming: {end_time -  start_time}")


        test_rewards.append(np.mean(queue_list[-100000:]))
        if (i_episode+1) % 5 == 0:
            data = np.array(test_rewards)
            df = pd.DataFrame(data=data,columns=["Average Queue"]).reset_index()
            df.to_csv(f'./{args.log_dir}/progress_{args.virtual}_seed{args.seed}_train_u_{args.uniform}.csv', index = False)
            np.save(f"./{args.log_dir}/{file_name}/queue_lists",queue_list)
        if (i_episode + 1 ) % 20 == 0:
            time_con = end_time - start_time
            avgr, avgb1, avgb2, avgb3 = test_policy(agent,scaler,service_rates,arrival_rates)
            results = [i_episode, total_numsteps, avgr, avgb1, avgb2, avgb3,  np.mean(total_reward,axis=0), np.mean(queue_list), time_con ]
            df = pd.DataFrame(data=[results],
                              columns=["i_episode", "total_numsteps", "avg_test_reward", "avg_test_b1", "avg_test_b2", "avg_test_b3",
                                       "avg_training_reward", "avg_traing_queuue_length", "time_consuming"])
            if not os.path.exists(
                    f'./{args.log_dir}/{file_name}/progress_test.csv'):
                df.to_csv(
                    f'./{args.log_dir}/{file_name}/progress_test.csv',index=False)
            else:
                df.to_csv(
                    f'./{args.log_dir}/{file_name}/progress_test.csv',index=False, mode='a', header=False)


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    #network = pn.ProcessingNetwork.from_name('criss_cross') # queuing network declaration
    #end_time = datetime.datetime.now()
    #time_policy = end_time - start_time
    #print('time of queuing network object creation:', int((time_policy.total_seconds() / 60) * 100) / 100., 'minutes')
    #network_id = ray.put(network)
    parser = argparse.ArgumentParser(description=('Train policy for a queueing network'))
    parser.add_argument('--env-name', default="queuing_rl")
    parser.add_argument('-g', '--gamma', type=float, help='Discount factor',
                        default = 0.99)
    parser.add_argument('--batch_size', type=int, help='Number of episodes per training batch',
                        default = 64)
    parser.add_argument('--batch_size_v', type=int, help='Number of episodes per training batch',
                        default = 400)
    parser.add_argument('--virtual_loop', type=int, help='Number of virtual batch_size',
                        default = 100)
    parser.add_argument('-m', '--hidden_size', type=int, help='Size of first hidden layer for value and policy NNs',
                        default = 64)
    parser.add_argument('--buffer_size', type=int, help='Size of buffer size',
                        default = 50)
    parser.add_argument('-t', '--total_steps', type=int, help='Number of total time-steps',
                        default = int(10**6))
                        #default = int(0.75 * 10**7))
    parser.add_argument('--update_frequence', type=int, help='frequency of updating networks',
                        default = 5000)
    parser.add_argument('--u_num', type=int, help='number of uniformly distributed samples',
                        default =90000)
    parser.add_argument('--test_frequence', type=int, help='frequency of testing',
                        default = 3000)
    parser.add_argument('-check','--check', action='store_true', help='whether sanity check')
    parser.add_argument('-s', '--seed', type=int, help='random seed',
                        default = 1234)
    parser.add_argument("--log_dir", default="temp_neural_2phase")
    parser.add_argument('--tau', type=float, default=0.005, metavar='G',
                    help='target smoothing coefficient(τ) (default: 0.005)')
    parser.add_argument('--service', type=float, default=1.5   , metavar='G')
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
    parser.add_argument('--updateone', action="store_true",
                    help='update one step or not')
    parser.add_argument('--virtual', action="store_true",
                    help='use virtual queues')
    parser.add_argument('--distributed', action="store_true",
                    help='use distributed-virtual queues')
    parser.add_argument('--policy', default="Gaussian",
                    help='Policy Type: Gaussian | Deterministic (default: Gaussian)')
    parser.add_argument('--target_update_interval', type=int, default=1, metavar='N',
                    help='Value target update per no. of updates per step (default: 1)')
    parser.add_argument('--start_steps', type=int, default=10000, metavar='N',
                    help='Steps sampling random actions (default: 10000)')
    parser.add_argument('--dis_train_step', type=int, default=10000, metavar='N',
                    help='Steps training distribution network (default: 10000)')
    parser.add_argument('--uniform', action="store_true",
                    help='use uniform distributed-virtual queues')
    args = parser.parse_args()
    file_name = f"seed_{args.seed}"
    import json
    import os
    if not os.path.exists(
        f'./{args.log_dir}/{file_name}'):
        os.makedirs(
        f'./{args.log_dir}/{file_name}')
    with open(f'./{args.log_dir}/{file_name}/args.txt', 'w') as fp:
        json.dump(args.__dict__, fp, indent=2)
    main(args)
