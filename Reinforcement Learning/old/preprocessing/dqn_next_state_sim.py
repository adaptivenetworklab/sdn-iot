import pandas as pd
import numpy as np
import random
import argparse
import os

# --- Constants & Configuration ---
TOTAL_BANDWIDTH = 100.0  # Mbps (Total capacity of the link/OVS)
BASE_DELAY_MS = 2.0      # Base wire latency
PACKET_SIZE_KB = 1.0     # Assumption for converting Mbps to Packet Count if missing

# Action Space: FlowVisor Slicing Policies
# Format: {Slice_Name: (Bandwidth_Limit_Percent, Priority_Queue_Level)}
ACTIONS = {
    0: {"camera": (70, 2), "heart_rate": (20, 1), "dht11": (10, 0)},  # Prio Camera
    1: {"camera": (30, 1), "heart_rate": (60, 2), "dht11": (10, 0)},  # Prio HR
    2: {"camera": (25, 0), "heart_rate": (25, 1), "dht11": (50, 2)},  # Prio DHT
    3: {"camera": (33, 1), "heart_rate": (33, 1), "dht11": (33, 1)},  # Balanced
}

SLA_MAX_DELAY = {
    "camera": 500.0,
    "heart_rate": 100.0,  # Critical!
    "dht11": 1000.0
}

class DataLoader:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def load(self):
        if not os.path.exists(self.csv_path):
            print(f"[WARN] File {self.csv_path} not found. Generating MOCK data.")
            return self.generate_mock_data()
        
        df = pd.read_csv(self.csv_path)
        # Normalize column names just in case
        df.columns = [c.strip().lower() for c in df.columns]
        return df

    def generate_mock_data(self):
        # Fallback for testing logic without real CSV
        dates = pd.date_range(start='2024-01-01', periods=100, freq='1S')
        data = {
            'timestamp': dates,
            'rx_mbps_p1': np.random.uniform(0.1, 5.0, 100), # DHT
            'rx_mbps_p2': np.abs(np.random.normal(5.0, 2.0, 100)), # Camera
            'rx_mbps_p4': np.random.uniform(0.1, 1.0, 100), # HR
            # Add delay columns if the real CSV has them, though we simulate 'Next Delay'
            'delay_ms_p1': np.random.uniform(5, 15, 100),
            'delay_ms_p2': np.random.uniform(10, 50, 100),
            'delay_ms_p4': np.random.uniform(2, 8, 100),
        }
        return pd.DataFrame(data)

class NetworkSim:
    def __init__(self):
        pass

    def calculate_next_state(self, current_demand, action_id):
        """
        Simulates the Network Physics.
        Input:
            current_demand: dict {'camera': mbps, 'heart_rate': mbps, 'dht11': mbps}
            action_id: int (0-3)
        Output:
            next_state: dict contains simulated delay, bandwidth, etc.
        """
        policy = ACTIONS[action_id]
        next_stats = {}
        
        total_prio_reward = 0
        violation_penalty = 0

        for sensor, demand_mbps in current_demand.items():
            # Get Switch Policy for this sensor
            alloc_percent, prio_level = policy.get(sensor, (10, 0))
            alloc_mbps = (alloc_percent / 100.0) * TOTAL_BANDWIDTH
            
            # 1. Bandwidth Simulation
            # If demand < allocated, we use demand. If demand > allocated, we cap at allocated.
            # But in reality, if demand > alloc, queues build up -> delay spikes.
            throughput = min(demand_mbps, alloc_mbps)
            
            # 2. Delay Simulation (Queueing Theory Approx: M/M/1)
            # Delay = 1 / (Service_Rate - Arrival_Rate)
            # Here: Service_Rate = Alloc_BW, Arrival_Rate = Demand
            # We add a epsilon to avoid div by zero
            congestion_margin = alloc_mbps - demand_mbps
            
            if congestion_margin > 0.5:
                # Uncongested: Base delay + small serialization delay
                simulated_delay = BASE_DELAY_MS + (1.0 / congestion_margin) * 10 
            else:
                # Congested! Delay grows exponentially with overload
                overload_factor = abs(congestion_margin)
                simulated_delay = BASE_DELAY_MS + 50.0 + (overload_factor * 20.0)
            
            # Priority bonus: High priority queues get processed faster (lower effective delay)
            if prio_level == 2:
                simulated_delay *= 0.7 # 30% faster
            elif prio_level == 1:
                simulated_delay *= 0.9 # 10% faster
                
            # Random jitter
            simulated_delay += np.random.uniform(-1.0, 1.0)
            simulated_delay = max(0.1, simulated_delay)

            # 3. Packet Count Estimation (if not in CSV)
            # Mbps = (Packets/sec * Size_bits) / 1e6
            pkt_count = (throughput * 1e6) / (PACKET_SIZE_KB * 8 * 1024) 

            # Update Next State Dict
            next_stats[f"bw_{sensor}"] = throughput
            next_stats[f"delay_{sensor}"] = simulated_delay
            next_stats[f"pkt_{sensor}"] = int(pkt_count)
            next_stats[f"prio_{sensor}"] = prio_level # State tracks current priority!

            # 4. Calculate Reward Component for this sensor
            # Reward = +1 if SLA met, -10 if violated
            sla = SLA_MAX_DELAY.get(sensor, 1000)
            if simulated_delay > sla:
                violation_penalty -= 5.0 # Penalty per violation
                if sensor == "heart_rate": # Critical!
                    violation_penalty -= 20.0
            else:
                # Reward for low latency, scaled
                total_prio_reward += (sla - simulated_delay) / sla 

        # Total Reward
        # We want to maximize Throughput and Minimize Delay
        # reward = total_throughput + total_prio_reward + violation_penalty
        reward = total_prio_reward + violation_penalty
        
        return next_stats, reward

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="d:/Kuliah/Semester 6/Riset/sdn-iot/DQN/dataset.csv", help="Input logs")
    parser.add_argument("--output", default="dqn_training_data.csv", help="Output RL Dataset")
    parser.add_argument("--mock", action="store_true", help="Use mock data if file not found")
    args = parser.parse_args()

    # 1. Load Data
    loader = DataLoader(args.input)
    if args.mock:
        df = loader.generate_mock_data()
    else:
        df = loader.load()

    print(f"[INFO] Loaded {len(df)} rows of traffic traces.")
    
    # 2. Main Simulation Loop
    experience_buffer = []
    
    # Mapping CSV columns to Sensor Names
    # Adjust these based on your specific CSV header format!
    # User CSV: rx_mbps_p1 (dht), rx_mbps_p2 (cam), rx_mbps_p4 (hr) (Deduced from User Context)
    # Re-verifying from user context:
    # P1 = 1 (DHT?) -> Earlier script said P1=DHT, P2=Cam, P4=HR.
    # dataset.csv header: rx_mbps_p1, rx_mbps_p2, rx_mbps_p4
    
    # Let's clean NaN
    df = df.fillna(0)

    for i in range(len(df) - 1):
        row = df.iloc[i]
        
        # Demand State (from Real World CSV)
        # We treat 'rx_mbps' as the Demand arriving at the switch
        demand = {
            "dht11": row.get('rx_mbps_p1', 0.1),
            "camera": row.get('rx_mbps_p2', 0.1), 
            "heart_rate": row.get('rx_mbps_p4', 0.1)
        }
        
        # State at Time T (Context)
        # We include the 'observed' delays from data to help model context, 
        # BUT for RL training, we often care about the transition caused by the action.
        # Let's define State Vector components:
        state_base = {
            "bw_camera": demand['camera'],
            "bw_hr": demand['heart_rate'],
            "bw_dht": demand['dht11'],
            "delay_camera": row.get('delay_ms_p2', 5.0), # Current observed delay
            "delay_hr": row.get('delay_ms_p4', 2.0),
            "delay_dht": row.get('delay_ms_p1', 5.0),
        }

        sim = NetworkSim()

        # Data Augmentation: Simulate ALL actions for this timestamp
        # This creates a "Counterfactual" dataset
        for action in range(4): # 0, 1, 2, 3
            
            # --- EXECUTE ACTION & GET NEXT STATE ---
            next_vals, reward = sim.calculate_next_state(demand, action)
            
            # Construct Transition Tuple
            transition = {
                # Current State (S)
                "cur_bw_cam": state_base['bw_camera'],
                "cur_bw_hr": state_base['bw_hr'],
                "cur_bw_dht": state_base['bw_dht'],
                "cur_delay_cam": state_base['delay_camera'],
                "cur_delay_hr": state_base['delay_hr'],
                "cur_delay_dht": state_base['delay_dht'],
                
                # We assume current priority was 'Balanced' (3) or unknown - 
                # but for Markov chain, we essentially input "Traffic State".
                
                # Action (A)
                "action": action,
                
                # Reward (R)
                "reward": round(reward, 4),
                
                # Next State (S')
                "next_bw_cam": next_vals['bw_camera'],
                "next_bw_hr": next_vals['bw_heart_rate'],
                "next_bw_dht": next_vals['bw_dht11'],
                "next_delay_cam": next_vals['delay_camera'],
                "next_delay_hr": next_vals['delay_heart_rate'],
                "next_delay_dht": next_vals['delay_dht11'],
                
                # New State Features
                "next_prio_cam": next_vals['prio_camera'],
                "next_prio_hr": next_vals['prio_heart_rate'],
                "next_prio_dht": next_vals['prio_dht11'],
                "next_pkt_cam": next_vals['pkt_camera'],
                "next_pkt_hr": next_vals['pkt_heart_rate'],
                "next_pkt_dht": next_vals['pkt_dht11'],
                
                "done": False # Continuous task usually
            }
            
            experience_buffer.append(transition)

    # 3. Save to CSV
    out_df = pd.DataFrame(experience_buffer)
    out_df.to_csv(args.output, index=False)
    print(f"[SUCCESS] Generated {len(out_df)} RL transitions.")
    print(f"         Saved to: {args.output}")
    print("         Columns:", list(out_df.columns))

if __name__ == "__main__":
    main()
