import os
import torch
import torch.nn.functional as F
from torch.optim import Adam
import numpy as np
from utils import soft_update, hard_update
from model import GaussianPolicy, QNetwork, DeterministicPolicy , GaussianPolicy_discrete
from model import DQNNET
from aprox_sd_two import Stationary
from scipy import special

class SAC_neural(object):
    def __init__(self, num_inputssi, action_dim, args):

        self.gamma = args.gamma
        self.tau = args.tau
        self.alpha = args.alpha

        self.policy_type = args.policy
        self.target_update_interval = args.target_update_interval
        self.automatic_entropy_tuning = args.automatic_entropy_tuning

        #self.device = torch.device("cuda" if args.cuda else "cpu")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        #self.critic = QNetwork(num_inputssi * 3, action_dim, args.hidden_size).to(device=self.device)
        self.critic = DQNNET(num_inputssi * 3, action_dim, args.hidden_size).to(device=self.device)
        self.critic_optim = Adam(self.critic.parameters(), lr=args.lr)

        self.critic_target = DQNNET(num_inputssi * 3, action_dim, args.hidden_size).to(self.device)
        hard_update(self.critic_target, self.critic)
        self.args = args
        self.aprox_SD = Stationary()

        if self.policy_type == "Gaussian":
            # Target Entropy = −dim(A) (e.g. , -6 for HalfCheetah-v2) as given in the paper
            if self.automatic_entropy_tuning is True:
                self.target_entropy = -torch.prod(torch.Tensor(action_dim).to(self.device)).item()
                self.log_alpha = torch.zeros(1, requires_grad=True, device=self.device)
                self.alpha_optim = Adam([self.log_alpha], lr=args.lr)

            self.policy = GaussianPolicy_discrete(num_inputssi * 3, action_dim, args.hidden_size).to(self.device)
            #self.policy = GaussianPolicy(num_inputs, action_space.n, args.hidden_size)
            self.policy_optim = Adam(self.policy.parameters(), lr=args.lr)

        else:
            self.alpha = 0
            self.automatic_entropy_tuning = False
            self.policy = DeterministicPolicy(num_inputssr, action_space.n, args.hidden_size)
            self.policy_optim = Adam(self.policy.parameters(), lr=args.lr)

    def select_action(self, sa, sr, sv, evaluate=False):

        arrival = torch.FloatTensor(sa).to(self.device)
        queue = torch.FloatTensor(sr).to(self.device)
        service = torch.FloatTensor(sv).to(self.device)

        state = torch.cat([arrival, queue, service]).to(self.device).unsqueeze(0)
        action = self.critic(state).data.max(1)[1].detach().cpu().numpy()

        #if np.sum(ql) == 0:
        #    return action
        #if ql[int(action)] == 0:
        #    zeros = np.where(ql != 0)[0]
        #    if len(zeros) >= 1:
        #        action = np.random.choice(zeros,1)[0]
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

    #agent.update_parameters(memory, memory_u, args.batch_size, scaler, args, ss_, tt, i_episode)
    def update_parameters(self,memory, memory_u, batch_size, scaler, scaler_a, scaler_v, args, updates, sd_updates, capacity):
    #def update_parameters(self, memory, memory_u, batch_size, scaler, args, updates, sd_updates,i_episode):
    #def update_parameters(self, memory, batch_size, scaler, scaler_a, scaler_v, args, capacity):
        # Sample a batch from memory
        if len(memory) < batch_size:
            return
        __sa_batch, __sr_batch, __sv_batch, __action_batch, __reward_batch, __next_sa_batch, __next_sr_batch, __next_sv_batch, __mask_batch = memory.sample_two(batch_size=batch_size)
        scale, offset = scaler.get()
        scale_a, offset_a = scaler_a.get()
        scale_v, offset_v = scaler_v.get()
        zero_ind = np.any(__sr_batch==0,axis=1)
        sa_batch = __sa_batch[~zero_ind]
        sr_batch = __sr_batch[~zero_ind]
        sv_batch = __sv_batch[~zero_ind]
        action_batch = __action_batch[~zero_ind]
        reward_batch = __reward_batch[~zero_ind]
        next_sa_batch = __next_sa_batch[~zero_ind]
        next_sr_batch = __next_sr_batch[~zero_ind]
        next_sv_batch = __next_sv_batch[~zero_ind]
        mask_batch = __mask_batch[~zero_ind]
        batch_size_ = sa_batch.shape[0]
        if batch_size_ == 0:
            scaled_sr = (__sr_batch - offset) * scale
            next_scaled_sr = (__next_sr_batch - offset) * scale

            scaled_sa = (__sa_batch - offset_a ) * scale_a
            next_scaled_sa = (__next_sa_batch - offset_a) * scale_a

            scaled_sv = (__sv_batch - offset_v) * scale_v
            next_scaled_sv = (__next_sv_batch - offset_v) * scale_v

            sr_batch_r = torch.FloatTensor(scaled_sr).to(self.device)
            sa_batch_r = torch.FloatTensor(scaled_sa).to(self.device)
            sv_batch_r = torch.FloatTensor(scaled_sv).to(self.device)

            next_sr_batch_r = torch.FloatTensor(next_scaled_sr).to(self.device)
            next_sa_batch_r = torch.FloatTensor(next_scaled_sa).to(self.device)
            next_sv_batch_r = torch.FloatTensor(next_scaled_sv).to(self.device)

            action_batch_r = torch.LongTensor(__action_batch).to(self.device).unsqueeze(1)
            reward_batch_r = torch.FloatTensor(__reward_batch).to(self.device).unsqueeze(1)

        else:
            if args.virtual:
                #sa_batch_ = np.tile(sa_batch,(args.batch_size_v - 1, 1)) #repeat 123123
                sa_batch_ = np.repeat(sa_batch,args.batch_size_v - 1, axis=0) #repeat 123123
                #sa_batch_ = sa_batch.repeat(args.batch_size_v - 1, 1)
                #sv_batch_ = np.tile(sv_batch,(args.batch_size_v - 1, 1)) #repeat 123123
                sv_batch_ = np.repeat(sv_batch,args.batch_size_v - 1, axis=0) #repeat 123123
                #print(action_batch[0:5])
                #print(sv_batch[0:5])
                indexlist = np.hstack([np.arange(batch_size_).reshape(batch_size_,1),action_batch.reshape(batch_size_,1)])
                #print(indexlist)
                sv_batch_real = np.zeros((batch_size_,3))
                sv_batch_real[tuple(indexlist.T.tolist())] = sv_batch[tuple(indexlist.T.tolist())]
                #sv_batch_real = np.tile(sv_batch_real,(args.batch_size_v - 1, 1)) #repeat 123123
                sv_batch_real = np.repeat(sv_batch_real,args.batch_size_v-1,axis=0) #repeat 123123

                change_batch_ = sa_batch_ - sv_batch_real
                if args.uniform:
                    virtual_sr_= np.random.uniform(low = 1.0,high = args.sample_size, size = (3,args.batch_size_v - 1) ).clip(1, args.sample_size -1)
                    virtual_sr_ = np.transpose(virtual_sr_).astype(int)
                else:
                    virtual_sr_= [np.random.normal(offset[n], 1. / scale[n], batch_size_ * (args.batch_size_v - 1)).clip(1,args.buffer_size - 1) for n in np.arange(len(capacity))]
                    virtual_sr_ = np.transpose(virtual_sr_).astype(int).clip(1,args.buffer_size)

                virtual_sr_batch = np.vstack([__sr_batch, virtual_sr_])
                next_virtual_sr_ = (virtual_sr_ + change_batch_).clip(0,args.buffer_size)

                virtual_next_sr_batch = np.vstack([__next_sr_batch, next_virtual_sr_])
                #print(virtual_sr_batch.shape,virtual_next_sr_batch.shape)

                virtual_reward_ = np.array((-np.sum(next_virtual_sr_,axis=1)) / (20)).reshape(next_virtual_sr_.shape[0],1)
                virtual_reward_ = np.clip(virtual_reward_,a_min = -30, a_max = None)

                __reward_batch = __reward_batch.reshape(batch_size,1)
                virtual_reward_batch = np.vstack([__reward_batch, virtual_reward_])
                __action_batch = __action_batch.reshape(batch_size,1)
                action_batch = action_batch.reshape(batch_size_,1)

                virtual_action_ = np.repeat(action_batch,args.batch_size_v - 1,axis=0).reshape(batch_size_ * (args.batch_size_v - 1),1)
                #virtual_action_ = action_batch.repeat(args.batch_size_v - 1,1).reshape(batch_size_ * (args.batch_size_v - 1) ,1)
                virtual_action_batch = np.vstack([__action_batch, virtual_action_])
                #virtual_action_batch = action_batch.repeat(args.batch_size_v,1).reshape(batch_size * args.batch_size_v ,1)

                sa_batch_ = np.vstack([__sa_batch, sa_batch_])
                sv_batch_ = np.vstack([__sv_batch, sv_batch_])

                #next_sa_batch_ = np.tile(next_sa_batch,(args.batch_size_v - 1, 1)) #repeat 123123
                next_sa_batch_ = np.repeat(next_sa_batch,args.batch_size_v - 1, axis=0) #repeat 123123
                #next_sv_batch_ = np.tile(next_sv_batch,(args.batch_size_v - 1, 1)) #repeat 123123
                next_sv_batch_ = np.repeat(next_sv_batch,args.batch_size_v - 1, axis=0) #repeat 123123
                next_sa_batch_ = np.vstack([__next_sa_batch, next_sa_batch_])
                next_sv_batch_ = np.vstack([__next_sv_batch, next_sv_batch_])

                #print(sa_batch_.shape,virtual_sr_batch.shape,sv_batch_.shape,virtual_next_sr_batch.shape)
                #print(virtual_reward_batch.shape,virtual_action_batch.shape)
                scaled_sr = (virtual_sr_batch - offset) * scale
                next_scaled_sr = (virtual_next_sr_batch - offset) * scale
                scaled_sa = (sa_batch_ - offset_a ) * scale_a
                next_scaled_sa = (next_sa_batch_ - offset_a) * scale_a
                scaled_sv = (sv_batch_ - offset_v) * scale_v
                next_scaled_sv = (next_sv_batch_ - offset_v) * scale_v


                sr_batch_r = torch.FloatTensor(scaled_sr).to(self.device)
                sa_batch_r = torch.FloatTensor(scaled_sa).to(self.device)
                sv_batch_r = torch.FloatTensor(scaled_sv).to(self.device)

                next_sr_batch_r = torch.FloatTensor(next_scaled_sr).to(self.device)
                next_sa_batch_r = torch.FloatTensor(next_scaled_sa).to(self.device)
                next_sv_batch_r = torch.FloatTensor(next_scaled_sv).to(self.device)

                action_batch_r = torch.LongTensor(virtual_action_batch).to(self.device)
                reward_batch_r = torch.FloatTensor(virtual_reward_batch).to(self.device)

            else:
                scaled_sr = (__sr_batch - offset) * scale
                next_scaled_sr = (__next_sr_batch - offset) * scale

                scaled_sa = (__sa_batch - offset_a ) * scale_a
                next_scaled_sa = (__next_sa_batch - offset_a) * scale_a

                scaled_sv = (__sv_batch - offset_v) * scale_v
                next_scaled_sv = (__next_sv_batch - offset_v) * scale_v

                sr_batch_r = torch.FloatTensor(scaled_sr).to(self.device)
                sa_batch_r = torch.FloatTensor(scaled_sa).to(self.device)
                sv_batch_r = torch.FloatTensor(scaled_sv).to(self.device)

                next_sr_batch_r = torch.FloatTensor(next_scaled_sr).to(self.device)
                next_sa_batch_r = torch.FloatTensor(next_scaled_sa).to(self.device)
                next_sv_batch_r = torch.FloatTensor(next_scaled_sv).to(self.device)

                action_batch_r = torch.LongTensor(__action_batch).to(self.device).unsqueeze(1)
                reward_batch_r = torch.FloatTensor(__reward_batch).to(self.device).unsqueeze(1)


        state_batch = torch.cat((sa_batch_r, sr_batch_r, sv_batch_r), 1).to(self.device)
        next_state_batch = torch.cat([next_sa_batch_r, next_sr_batch_r, next_sv_batch_r] , 1).to(self.device)

        """Calculates the losses for the two critics. This is the ordinary Q-learning loss except the additional entropy
         term is taken into account"""


        with torch.no_grad():
            target_Q = self.critic_target(next_state_batch).detach().max(1)[0]
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
        return qf_loss.item()
        #return qf1_loss.item(), qf2_loss.item(), policy_loss.item(), alpha_loss.item(), alpha_tlogs.item()

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
