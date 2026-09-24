import json

with open('/home/habb/Kuliah/sdn-iot/Reinforcement Learning/revision/Preprocessing.ipynb', 'r') as f:
    nb = json.load(f)

# Update cell 1 (index 0) - config
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and 'SLA_DELAY_P4 = 10.0' in ''.join(cell['source']):
        new_source = []
        for line in cell['source']:
            new_source.append(line)
            if 'SLA_DELAY_P4 = 10.0' in line:
                new_source.append("SLA_DELAY_P1 = 100.0 # ms (Standard IoT)\n")
                new_source.append("SLA_DELAY_P2 = 50.0 # ms (Standard eMBB)\n")
        cell['source'] = new_source

# Update cell 2 (index 1) - calculate_sdh_reward
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code' and 'def calculate_sdh_reward' in ''.join(cell['source']):
        cell['source'] = [
            "def sigmoid_penalty(val, threshold, k=1.5):\n",
            "    \"\"\"Memberikan penalti yang smooth saat mendekati batas SLA.\"\"\"\n",
            "    # Semakin mendekati atau melewati threshold, nilai mendekati 1 (maksimal penalti)\n",
            "    return 1 / (1 + np.exp(-k * (val - threshold)))\n",
            "\n",
            "def calculate_sdh_reward(row):\n",
            "    # 1. URLLC (Port 4) - Kritis\n",
            "    # Penalti 10 poin per violation\n",
            "    penalty_p4 = 10 * sigmoid_penalty(row['delay_ms_p4'], threshold=SLA_DELAY_P4)\n",
            "    \n",
            "    # 2. IoT (Port 1) & eMBB (Port 2) - Penting tapi tidak mematikan\n",
            "    # Penalti 5 poin per violation\n",
            "    penalty_p1 = 5 * sigmoid_penalty(row['delay_ms_p1'], threshold=SLA_DELAY_P1)\n",
            "    penalty_p2 = 5 * sigmoid_penalty(row['delay_ms_p2'], threshold=SLA_DELAY_P2)\n",
            "    \n",
            "    # 3. eMBB (Port 2) - Throughput Incentive\n",
            "    # Normalisasi throughput: Semakin mendekati target 15Mbps, reward semakin besar\n",
            "    # Reward posifit 5 poin maksimal\n",
            "    r_throughput_p2 = 5 * np.clip(row['rx_mbps_p2'] / TARGET_THROUGHPUT_P2, 0, 1)\n",
            "    \n",
            "    # 4. Global Reliability (Packet Drops)\n",
            "    total_drop = row.get('drop_p1', 0) + row.get('drop_p2', 0) + row.get('drop_p4', 0)\n",
            "    p_drop = np.clip(total_drop, 0, 5) # Penalti langsung dari jumlah drop, max 5\n",
            "    \n",
            "    # FORMULASI TOTAL REWARD\n",
            "    reward = r_throughput_p2 - penalty_p4 - penalty_p1 - penalty_p2 - p_drop\n",
            "    \n",
            "    return reward\n"
        ]

with open('/home/habb/Kuliah/sdn-iot/Reinforcement Learning/revision/Preprocessing.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook modified successfully.")
