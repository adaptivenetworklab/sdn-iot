# Analisis V2 (val)

Dibangkitkan oleh `scripts/analyze_v2.py` dari `dryrun-v2-existing`. 172 run, 14 cell, seed per cell 2-20.

## Primer (Holm di dalam keluarga)

| family | X | Y | n | mean_X | mean_Y | mean_d | ci_lo | ci_hi | p_wilcoxon | p_ttest | p_holm | rank_biserial | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | PPO [full] safety on | PPO [full] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| a | SDH-PPO [full] safety on | SDH-PPO [full] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| a | DQN [full] safety on | DQN [full] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| a | DDQN [full] safety on | DDQN [full] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| a | demand_prop [full] safety on | demand_prop [full] safety off | 20 | 29.87 | 29.78 | 0.09167 | 0.008333 | 0.17 | 0.03994 | 0.04281 | 0.03994 | 0.5238 | X lebih buruk; selisih dalam [0.01, 0.17] |
| a | no_control [full] safety on | no_control [full] safety off | 20 | 32.61 | 60.04 | -27.43 | -29.04 | -25.79 | 1.907e-06 | 7.078e-18 | 7.629e-06 | -1 | X lebih baik; selisih dalam [-29.04, -25.79] |
| a | equal_split [full] safety on | equal_split [full] safety off | 20 | 37.79 | 51.61 | -13.82 | -14.17 | -13.47 | 1.907e-06 | 3.104e-25 | 7.629e-06 | -1 | X lebih baik; selisih dalam [-14.17, -13.47] |
| a | threshold [full] safety on | threshold [full] safety off | 20 | 65.81 | 67.06 | -1.248 | -1.377 | -1.123 | 8.832e-05 | 9.84e-14 | 0.0001766 | -1 | X lebih baik; selisih dalam [-1.38, -1.12] |
| b | SDH-PPO [full] safety on | demand_prop [full] safety on | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | PPO [full] safety off | PPO [real_only] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | PPO [full] safety off | PPO [aug_subsample] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | PPO [real_only] safety off | PPO [aug_subsample] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | SDH-PPO [full] safety off | SDH-PPO [real_only] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | SDH-PPO [full] safety off | SDH-PPO [aug_subsample] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | SDH-PPO [real_only] safety off | SDH-PPO [aug_subsample] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | DQN [full] safety off | DQN [real_only] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | DQN [full] safety off | DQN [aug_subsample] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | DQN [real_only] safety off | DQN [aug_subsample] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | DDQN [full] safety off | DDQN [real_only] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | DDQN [full] safety off | DDQN [aug_subsample] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| c | DDQN [real_only] safety off | DDQN [aug_subsample] safety off | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| e | SDH-PPO residual [full] safety on | demand_prop [full] safety on | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |
| e | SDH-PPO + BC init [full] safety on | demand_prop [full] safety on | 0 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | data tidak tersedia |

## Eksploratif (tanpa uji)

| family | X | Y | n | mean_d | ci_lo | ci_hi | verdict |
|---|---|---|---|---|---|---|---|
| d | SDH-PPO [full] safety on | SDH-PPO [no_dueling] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| d | SDH-PPO [full] safety off | SDH-PPO [no_dueling] safety off | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | PPO [full] safety on | PPO [real_only] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | PPO [full] safety on | PPO [aug_subsample] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | PPO [real_only] safety on | PPO [aug_subsample] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | SDH-PPO [full] safety on | SDH-PPO [real_only] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | SDH-PPO [full] safety on | SDH-PPO [aug_subsample] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | SDH-PPO [real_only] safety on | SDH-PPO [aug_subsample] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | DQN [full] safety on | DQN [real_only] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | DQN [full] safety on | DQN [aug_subsample] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | DQN [real_only] safety on | DQN [aug_subsample] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | DDQN [full] safety on | DDQN [real_only] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | DDQN [full] safety on | DDQN [aug_subsample] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |
| c_safetyon | DDQN [real_only] safety on | DDQN [aug_subsample] safety on | 0 | n/a | n/a | n/a | data tidak tersedia |

## IQM total violation (rliable, stratified bootstrap)

| cell | n | iqm_viol | ci_lo | ci_hi |
|---|---|---|---|---|
| bcsdhppo_full_safetyoff | 2 | 33.28 | 32.73 | 33.83 |
| ddqn_full_safetyoff | 2 | 35.98 | 35.70 | 36.27 |
| demand_prop_full_safetyoff | 20 | 29.73 | 27.38 | 32.07 |
| demand_prop_full_safetyon | 20 | 29.69 | 27.42 | 32.12 |
| dqn_full_safetyoff | 2 | 35.93 | 35.07 | 36.80 |
| equal_split_full_safetyoff | 20 | 51.63 | 50.12 | 53.07 |
| equal_split_full_safetyon | 20 | 37.72 | 35.79 | 39.64 |
| no_control_full_safetyoff | 20 | 60.09 | 58.50 | 61.48 |
| no_control_full_safetyon | 20 | 32.69 | 30.32 | 34.88 |
| ppo_full_safetyoff | 2 | 51.50 | 49.33 | 53.67 |
| ressdhppo_full_safetyoff | 2 | 33.10 | 32.53 | 33.67 |
| sdhppo_full_safetyoff | 2 | 51.58 | 50.97 | 52.20 |
| threshold_full_safetyoff | 20 | 67.06 | 66.05 | 68.10 |
| threshold_full_safetyon | 20 | 65.77 | 64.81 | 66.81 |

## Probability of improvement P(X lebih baik dari Y)

| pair | p_X_better | ci_lo | ci_hi |
|---|---|---|---|
| a: demand_prop_full_safetyon vs demand_prop_full_safetyoff | 0.49 | 0.30 | 0.67 |
| a: no_control_full_safetyon vs no_control_full_safetyoff | 1.00 | 1.00 | 1.00 |
| a: equal_split_full_safetyon vs equal_split_full_safetyoff | 1.00 | 1.00 | 1.00 |
| a: threshold_full_safetyon vs threshold_full_safetyoff | 0.69 | 0.51 | 0.84 |

## Sekunder

| cell | n | viol_total | viol_p1 | viol_p2 | viol_p4 | delay_p1 | delay_p2 | delay_p4 | drop_total | reward | res_mean_abs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bcsdhppo_full_safetyoff | 2 | 33.28 | 31.95 | 31.15 | 36.75 | 61.23 | 61.79 | 69.70 | 2.86 | -1.20 | n/a |
| ddqn_full_safetyoff | 2 | 35.98 | 24.65 | 50.35 | 32.95 | 43.48 | 98.36 | 59.21 | 3.39 | -1.02 | n/a |
| demand_prop_full_safetyoff | 20 | 29.78 | 30.38 | 28.54 | 30.41 | 56.74 | 55.58 | 57.02 | 2.50 | -1.05 | n/a |
| demand_prop_full_safetyon | 20 | 29.87 | 30.29 | 28.77 | 30.54 | 56.86 | 56.30 | 58.34 | 2.47 | -1.06 | n/a |
| dqn_full_safetyoff | 2 | 35.93 | 18.75 | 52.25 | 36.80 | 29.00 | 102.64 | 70.04 | 3.39 | -0.98 | n/a |
| equal_split_full_safetyoff | 20 | 51.61 | 29.64 | 27.61 | 97.58 | 55.09 | 53.83 | 158.66 | 2.52 | -1.77 | n/a |
| equal_split_full_safetyon | 20 | 37.79 | 29.86 | 28.37 | 55.14 | 56.17 | 55.15 | 66.17 | 2.47 | -1.10 | n/a |
| no_control_full_safetyoff | 20 | 60.04 | 59.87 | 55.49 | 64.76 | 117.24 | 110.42 | 127.80 | 4.64 | -2.22 | n/a |
| no_control_full_safetyon | 20 | 32.61 | 32.67 | 30.84 | 34.31 | 60.53 | 60.78 | 63.90 | 2.55 | -1.14 | n/a |
| ppo_full_safetyoff | 2 | 51.50 | 25.00 | 97.85 | 31.65 | 45.41 | 195.64 | 50.68 | 4.89 | -1.10 | n/a |
| ressdhppo_full_safetyoff | 2 | 33.10 | 33.55 | 30.55 | 35.20 | 63.24 | 60.40 | 66.82 | 2.86 | -22.80 | 0.14 |
| sdhppo_full_safetyoff | 2 | 51.58 | 53.40 | 76.45 | 24.90 | 104.62 | 152.22 | 35.48 | 4.71 | -1.46 | n/a |
| threshold_full_safetyoff | 20 | 67.06 | 67.64 | 65.00 | 68.55 | 99.63 | 114.06 | 102.60 | 2.62 | -1.75 | n/a |
| threshold_full_safetyon | 20 | 65.81 | 67.53 | 61.46 | 68.44 | 99.35 | 111.71 | 102.39 | 2.62 | -1.75 | n/a |

## Skenario non-stasioner (eksploratif)

| cell | n | viol_total |
|---|---|---|
| bcsdhppo_full_safetyoff | 2 | 33.28 |
| ddqn_full_safetyoff | 2 | 35.98 |
| demand_prop_full_safetyoff | 20 | 29.78 |
| demand_prop_full_safetyon | 20 | 29.87 |
| dqn_full_safetyoff | 2 | 35.93 |
| equal_split_full_safetyoff | 20 | 51.61 |
| equal_split_full_safetyon | 20 | 37.79 |
| no_control_full_safetyoff | 20 | 60.04 |
| no_control_full_safetyon | 20 | 32.61 |
| ppo_full_safetyoff | 2 | 51.50 |
| ressdhppo_full_safetyoff | 2 | 33.10 |
| sdhppo_full_safetyoff | 2 | 51.58 |
| threshold_full_safetyoff | 20 | 67.06 |
| threshold_full_safetyon | 20 | 65.81 |

## Sensitivitas ambang SLA (eksploratif; kebijakan dilatih pada 6/70/7)

| cell | viol_total | sens_0.5x | sens_0.75x | sens_1.5x | sens_2x | sens_real_train_median |
|---|---|---|---|---|---|---|
| bcsdhppo_full_safetyoff | 33.28 | 33.82 | 33.67 | 33.05 | 32.77 | 33.98 |
| ddqn_full_safetyoff | 35.98 | 36.88 | 36.48 | 35.12 | 34.57 | 37.93 |
| demand_prop_full_safetyoff | 29.77 | 29.87 | 29.83 | 29.40 | 29.36 | 30.12 |
| demand_prop_full_safetyon | 29.87 | 30.14 | 29.92 | 29.57 | 29.48 | 30.24 |
| dqn_full_safetyoff | 35.93 | 37.03 | 36.58 | 35.00 | 34.42 | 37.85 |
| equal_split_full_safetyoff | 51.61 | 51.82 | 51.75 | 51.25 | 50.92 | 51.87 |
| equal_split_full_safetyon | 37.79 | 40.02 | 39.31 | 36.25 | 33.30 | 38.23 |
| no_control_full_safetyoff | 60.04 | 60.17 | 60.09 | 59.90 | 59.79 | 60.22 |
| no_control_full_safetyon | 32.61 | 33.19 | 32.85 | 32.22 | 31.82 | 33.79 |
| ppo_full_safetyoff | 51.50 | 51.67 | 51.60 | 51.38 | 51.25 | 51.65 |
| ressdhppo_full_safetyoff | 33.10 | 33.42 | 33.35 | 32.90 | 32.73 | 33.73 |
| sdhppo_full_safetyoff | 51.58 | 51.92 | 51.70 | 51.38 | 51.08 | 51.98 |
| threshold_full_safetyoff | 67.06 | 71.76 | 69.35 | 62.65 | 58.94 | 74.09 |
| threshold_full_safetyon | 65.81 | 69.67 | 67.72 | 62.73 | 59.67 | 71.68 |
