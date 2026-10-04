# Analisis V2 (test)

Dibangkitkan oleh `scripts/analyze_v2.py` dari `final-v2`. 760 run, 38 cell, seed per cell 20-20.

## Primer (Holm di dalam keluarga)

| family | X | Y | n | mean_X | mean_Y | mean_d | ci_lo | ci_hi | p_wilcoxon | p_ttest | p_holm | rank_biserial | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a | PPO [full] safety on | PPO [full] safety off | 20 | 42.83 | 51.5 | -8.67 | -11.05 | -6.26 | 9.537e-06 | 1.291e-06 | 4.768e-05 | -0.9714 | X lebih baik; selisih dalam [-11.05, -6.26] |
| a | SDH-PPO [full] safety on | SDH-PPO [full] safety off | 20 | 42.47 | 51.52 | -9.052 | -10.43 | -7.552 | 1.907e-06 | 3.076e-10 | 1.526e-05 | -1 | X lebih baik; selisih dalam [-10.43, -7.55] |
| a | DQN [full] safety on | DQN [full] safety off | 20 | 44.3 | 44.44 | -0.1383 | -1.8 | 1.547 | 0.6477 | 0.8758 | 0.6477 | -0.1238 | tidak signifikan; selisih dalam [-1.80, 1.55] |
| a | DDQN [full] safety on | DDQN [full] safety off | 20 | 44.05 | 45.95 | -1.893 | -3.61 | -0.03833 | 0.07585 | 0.05655 | 0.1517 | -0.4571 | tidak signifikan; selisih dalam [-3.61, -0.04] |
| a | demand_prop [full] safety on | demand_prop [full] safety off | 20 | 33.75 | 33.87 | -0.1233 | -0.245 | -0.001667 | 0.04624 | 0.06682 | 0.1387 | -0.5211 | tidak signifikan; selisih dalam [-0.24, -0.00] |
| a | no_control [full] safety on | no_control [full] safety off | 20 | 37.34 | 60.91 | -23.57 | -25.3 | -21.79 | 1.907e-06 | 4.243e-16 | 1.526e-05 | -1 | X lebih baik; selisih dalam [-25.30, -21.79] |
| a | equal_split [full] safety on | equal_split [full] safety off | 20 | 43.16 | 52.39 | -9.225 | -9.63 | -8.82 | 1.907e-06 | 1.287e-20 | 1.526e-05 | -1 | X lebih baik; selisih dalam [-9.63, -8.82] |
| a | threshold [full] safety on | threshold [full] safety off | 20 | 68.9 | 70.01 | -1.105 | -1.292 | -0.9067 | 0.0001031 | 1.302e-09 | 0.0004122 | -0.9905 | X lebih baik; selisih dalam [-1.29, -0.91] |
| b | SDH-PPO [full] safety on | demand_prop [full] safety on | 20 | 42.47 | 33.75 | 8.72 | 7.595 | 9.788 | 1.907e-06 | 4.594e-12 | 1.907e-06 | 1 | X lebih buruk; selisih dalam [7.60, 9.79] |
| c | PPO [full] safety off | PPO [real_only] safety off | 20 | 51.5 | 51.07 | 0.4367 | -1.778 | 2.485 | 0.3603 | 0.6988 | 1 | 0.2333 | tidak signifikan; selisih dalam [-1.78, 2.49] |
| c | PPO [full] safety off | PPO [aug_subsample] safety off | 20 | 51.5 | 53.02 | -1.517 | -3.865 | 0.485 | 0.4114 | 0.1955 | 1 | -0.2095 | tidak signifikan; selisih dalam [-3.87, 0.49] |
| c | PPO [real_only] safety off | PPO [aug_subsample] safety off | 20 | 51.07 | 53.02 | -1.953 | -3.672 | -0.32 | 0.05937 | 0.03987 | 0.2968 | -0.481 | tidak signifikan; selisih dalam [-3.67, -0.32] |
| c | SDH-PPO [full] safety off | SDH-PPO [real_only] safety off | 20 | 51.52 | 51.46 | 0.05833 | -1.102 | 1.135 | 0.4114 | 0.9217 | 1 | 0.2095 | tidak signifikan; selisih dalam [-1.10, 1.14] |
| c | SDH-PPO [full] safety off | SDH-PPO [aug_subsample] safety off | 20 | 51.52 | 52.84 | -1.327 | -2.743 | -0.09496 | 0.114 | 0.0742 | 0.4559 | -0.4095 | tidak signifikan; selisih dalam [-2.74, -0.09] |
| c | SDH-PPO [real_only] safety off | SDH-PPO [aug_subsample] safety off | 20 | 51.46 | 52.84 | -1.385 | -2.347 | -0.4133 | 0.006205 | 0.01246 | 0.04964 | -0.7158 | X lebih baik; selisih dalam [-2.35, -0.41] |
| c | DQN [full] safety off | DQN [real_only] safety off | 20 | 44.44 | 41.56 | 2.878 | 0.91 | 4.782 | 0.01373 | 0.01079 | 0.0824 | 0.6286 | tidak signifikan; selisih dalam [0.91, 4.78] |
| c | DQN [full] safety off | DQN [aug_subsample] safety off | 20 | 44.44 | 37.98 | 6.462 | 5.193 | 7.717 | 3.815e-06 | 7.493e-09 | 4.196e-05 | 0.9905 | X lebih buruk; selisih dalam [5.19, 7.72] |
| c | DQN [real_only] safety off | DQN [aug_subsample] safety off | 20 | 41.56 | 37.98 | 3.583 | 1.69 | 5.543 | 0.002325 | 0.002219 | 0.02093 | 0.7429 | X lebih buruk; selisih dalam [1.69, 5.54] |
| c | DDQN [full] safety off | DDQN [real_only] safety off | 20 | 45.95 | 43.13 | 2.817 | 1.202 | 4.387 | 0.007296 | 0.003321 | 0.05107 | 0.6667 | tidak signifikan; selisih dalam [1.20, 4.39] |
| c | DDQN [full] safety off | DDQN [aug_subsample] safety off | 20 | 45.95 | 38.48 | 7.467 | 6.147 | 8.795 | 1.907e-06 | 1.427e-09 | 2.289e-05 | 1 | X lebih buruk; selisih dalam [6.15, 8.80] |
| c | DDQN [real_only] safety off | DDQN [aug_subsample] safety off | 20 | 43.13 | 38.48 | 4.65 | 2.92 | 6.478 | 0.0002188 | 8.037e-05 | 0.002188 | 0.9429 | X lebih buruk; selisih dalam [2.92, 6.48] |
| e | SDH-PPO residual [full] safety on | demand_prop [full] safety on | 20 | 33.81 | 33.75 | 0.065 | -0.2434 | 0.355 | 0.4812 | 0.6809 | 0.9625 | 0.1842 | tidak signifikan; selisih dalam [-0.24, 0.35] |
| e | SDH-PPO + BC init [full] safety on | demand_prop [full] safety on | 20 | 33.79 | 33.75 | 0.04 | -0.4734 | 0.6717 | 0.6435 | 0.8952 | 0.9625 | -0.1211 | tidak signifikan; selisih dalam [-0.47, 0.67] |

## Eksploratif (tanpa uji)

| family | X | Y | n | mean_d | ci_lo | ci_hi | verdict |
|---|---|---|---|---|---|---|---|
| d | SDH-PPO [full] safety on | SDH-PPO [no_dueling] safety on | 20 | -0.76 | -2.08 | 0.65 | selisih dalam [-2.08, 0.65] |
| d | SDH-PPO [full] safety off | SDH-PPO [no_dueling] safety off | 20 | -1.52 | -3.87 | 0.50 | selisih dalam [-3.87, 0.50] |
| c_safetyon | PPO [full] safety on | PPO [real_only] safety on | 20 | 0.60 | -1.47 | 2.61 | selisih dalam [-1.47, 2.61] |
| c_safetyon | PPO [full] safety on | PPO [aug_subsample] safety on | 20 | 1.97 | 0.16 | 3.81 | selisih dalam [0.16, 3.81] |
| c_safetyon | PPO [real_only] safety on | PPO [aug_subsample] safety on | 20 | 1.36 | -0.27 | 2.86 | selisih dalam [-0.27, 2.86] |
| c_safetyon | SDH-PPO [full] safety on | SDH-PPO [real_only] safety on | 20 | -0.79 | -2.46 | 0.89 | selisih dalam [-2.46, 0.89] |
| c_safetyon | SDH-PPO [full] safety on | SDH-PPO [aug_subsample] safety on | 20 | -1.12 | -2.38 | 0.25 | selisih dalam [-2.38, 0.25] |
| c_safetyon | SDH-PPO [real_only] safety on | SDH-PPO [aug_subsample] safety on | 20 | -0.32 | -2.14 | 1.41 | selisih dalam [-2.14, 1.41] |
| c_safetyon | DQN [full] safety on | DQN [real_only] safety on | 20 | 0.51 | -1.03 | 2.08 | selisih dalam [-1.03, 2.08] |
| c_safetyon | DQN [full] safety on | DQN [aug_subsample] safety on | 20 | 5.04 | 3.55 | 6.55 | selisih dalam [3.55, 6.55] |
| c_safetyon | DQN [real_only] safety on | DQN [aug_subsample] safety on | 20 | 4.53 | 3.54 | 5.53 | selisih dalam [3.54, 5.53] |
| c_safetyon | DDQN [full] safety on | DDQN [real_only] safety on | 20 | 0.67 | -1.21 | 2.57 | selisih dalam [-1.21, 2.57] |
| c_safetyon | DDQN [full] safety on | DDQN [aug_subsample] safety on | 20 | 4.77 | 3.41 | 6.24 | selisih dalam [3.41, 6.24] |
| c_safetyon | DDQN [real_only] safety on | DDQN [aug_subsample] safety on | 20 | 4.10 | 2.69 | 5.53 | selisih dalam [2.69, 5.53] |

## IQM total violation (rliable, stratified bootstrap)

| cell | n | iqm_viol | ci_lo | ci_hi |
|---|---|---|---|---|
| bcsdhppo_full_safetyoff | 20 | 36.08 | 34.08 | 39.88 |
| bcsdhppo_full_safetyon | 20 | 33.42 | 31.31 | 36.42 |
| ddqn_aug_subsample_safetyoff | 20 | 37.81 | 36.17 | 40.23 |
| ddqn_aug_subsample_safetyon | 20 | 39.20 | 36.82 | 42.00 |
| ddqn_full_safetyoff | 20 | 45.73 | 44.28 | 47.35 |
| ddqn_full_safetyon | 20 | 43.21 | 41.04 | 45.90 |
| ddqn_real_only_safetyoff | 20 | 43.14 | 40.51 | 45.87 |
| ddqn_real_only_safetyon | 20 | 42.67 | 40.97 | 45.35 |
| demand_prop_full_safetyoff | 20 | 33.36 | 31.45 | 35.95 |
| demand_prop_full_safetyon | 20 | 33.28 | 31.40 | 35.72 |
| dqn_aug_subsample_safetyoff | 20 | 37.66 | 35.05 | 40.25 |
| dqn_aug_subsample_safetyon | 20 | 39.02 | 36.76 | 41.24 |
| dqn_full_safetyoff | 20 | 44.44 | 42.39 | 46.64 |
| dqn_full_safetyon | 20 | 43.62 | 41.39 | 46.24 |
| dqn_real_only_safetyoff | 20 | 42.67 | 40.17 | 44.01 |
| dqn_real_only_safetyon | 20 | 43.49 | 42.07 | 45.57 |
| equal_split_full_safetyoff | 20 | 52.01 | 50.68 | 53.82 |
| equal_split_full_safetyon | 20 | 42.75 | 41.13 | 44.86 |
| no_control_full_safetyoff | 20 | 61.16 | 59.15 | 62.93 |
| no_control_full_safetyon | 20 | 36.94 | 35.16 | 39.04 |
| ppo_aug_subsample_safetyoff | 20 | 51.31 | 49.66 | 54.52 |
| ppo_aug_subsample_safetyon | 20 | 41.13 | 38.16 | 43.44 |
| ppo_full_safetyoff | 20 | 50.31 | 49.25 | 52.29 |
| ppo_full_safetyon | 20 | 42.89 | 40.73 | 44.88 |
| ppo_real_only_safetyoff | 20 | 50.02 | 48.24 | 52.63 |
| ppo_real_only_safetyon | 20 | 42.01 | 38.57 | 45.16 |
| ressdhppo_full_safetyoff | 20 | 33.89 | 31.92 | 36.34 |
| ressdhppo_full_safetyon | 20 | 33.47 | 31.35 | 35.74 |
| sdhppo_aug_subsample_safetyoff | 20 | 51.93 | 50.54 | 54.28 |
| sdhppo_aug_subsample_safetyon | 20 | 43.27 | 41.39 | 45.90 |
| sdhppo_full_safetyoff | 20 | 51.00 | 49.80 | 53.06 |
| sdhppo_full_safetyon | 20 | 42.28 | 39.69 | 45.21 |
| sdhppo_no_dueling_safetyoff | 20 | 51.61 | 49.68 | 54.60 |
| sdhppo_no_dueling_safetyon | 20 | 42.61 | 40.86 | 45.28 |
| sdhppo_real_only_safetyoff | 20 | 50.85 | 49.75 | 52.50 |
| sdhppo_real_only_safetyon | 20 | 43.40 | 40.80 | 45.76 |
| threshold_full_safetyoff | 20 | 69.78 | 69.12 | 70.72 |
| threshold_full_safetyon | 20 | 68.74 | 67.85 | 69.82 |

## Probability of improvement P(X lebih baik dari Y)

| pair | p_X_better | ci_lo | ci_hi |
|---|---|---|---|
| a: ppo_full_safetyon vs ppo_full_safetyoff | 0.90 | 0.78 | 0.99 |
| a: sdhppo_full_safetyon vs sdhppo_full_safetyoff | 0.93 | 0.83 | 0.99 |
| a: dqn_full_safetyon vs dqn_full_safetyoff | 0.55 | 0.37 | 0.73 |
| a: ddqn_full_safetyon vs ddqn_full_safetyoff | 0.66 | 0.48 | 0.83 |
| a: demand_prop_full_safetyon vs demand_prop_full_safetyoff | 0.52 | 0.34 | 0.70 |
| a: no_control_full_safetyon vs no_control_full_safetyoff | 1.00 | 1.00 | 1.00 |
| a: equal_split_full_safetyon vs equal_split_full_safetyoff | 0.94 | 0.85 | 1.00 |
| a: threshold_full_safetyon vs threshold_full_safetyoff | 0.66 | 0.48 | 0.82 |
| b: sdhppo_full_safetyon vs demand_prop_full_safetyon | 0.12 | 0.03 | 0.24 |
| c: ppo_full_safetyoff vs ppo_real_only_safetyoff | 0.46 | 0.28 | 0.64 |
| c: ppo_full_safetyoff vs ppo_aug_subsample_safetyoff | 0.56 | 0.38 | 0.74 |
| c: ppo_real_only_safetyoff vs ppo_aug_subsample_safetyoff | 0.60 | 0.42 | 0.77 |
| c: sdhppo_full_safetyoff vs sdhppo_real_only_safetyoff | 0.47 | 0.29 | 0.66 |
| c: sdhppo_full_safetyoff vs sdhppo_aug_subsample_safetyoff | 0.59 | 0.42 | 0.77 |
| c: sdhppo_real_only_safetyoff vs sdhppo_aug_subsample_safetyoff | 0.61 | 0.43 | 0.78 |
| c: dqn_full_safetyoff vs dqn_real_only_safetyoff | 0.34 | 0.18 | 0.53 |
| c: dqn_full_safetyoff vs dqn_aug_subsample_safetyoff | 0.17 | 0.05 | 0.30 |
| c: dqn_real_only_safetyoff vs dqn_aug_subsample_safetyoff | 0.29 | 0.13 | 0.47 |
| c: ddqn_full_safetyoff vs ddqn_real_only_safetyoff | 0.32 | 0.17 | 0.50 |
| c: ddqn_full_safetyoff vs ddqn_aug_subsample_safetyoff | 0.12 | 0.02 | 0.25 |
| c: ddqn_real_only_safetyoff vs ddqn_aug_subsample_safetyoff | 0.23 | 0.10 | 0.39 |
| e: ressdhppo_full_safetyon vs demand_prop_full_safetyon | 0.49 | 0.31 | 0.67 |
| e: bcsdhppo_full_safetyon vs demand_prop_full_safetyon | 0.50 | 0.32 | 0.69 |

## Sekunder

| cell | n | viol_total | viol_p1 | viol_p2 | viol_p4 | delay_p1 | delay_p2 | delay_p4 | drop_total | reward | res_mean_abs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| bcsdhppo_full_safetyoff | 20 | 36.87 | 31.84 | 45.95 | 32.83 | 60.34 | 88.18 | 60.12 | 2.69 | -1.13 | n/a |
| bcsdhppo_full_safetyon | 20 | 33.79 | 32.41 | 34.70 | 34.26 | 59.87 | 67.73 | 61.21 | 2.63 | -1.12 | n/a |
| ddqn_aug_subsample_safetyoff | 20 | 38.48 | 28.02 | 58.15 | 29.28 | 51.55 | 110.49 | 52.76 | 2.87 | -1.02 | n/a |
| ddqn_aug_subsample_safetyon | 20 | 39.28 | 31.46 | 51.32 | 35.05 | 58.30 | 95.80 | 61.32 | 2.68 | -1.12 | n/a |
| ddqn_full_safetyoff | 20 | 45.95 | 18.41 | 88.21 | 31.22 | 29.65 | 171.66 | 57.20 | 3.92 | -0.95 | n/a |
| ddqn_full_safetyon | 20 | 44.05 | 34.54 | 60.14 | 37.48 | 60.88 | 109.73 | 64.22 | 2.69 | -1.17 | n/a |
| ddqn_real_only_safetyoff | 20 | 43.13 | 20.60 | 74.19 | 34.59 | 34.62 | 143.05 | 56.21 | 3.60 | -0.95 | n/a |
| ddqn_real_only_safetyon | 20 | 43.38 | 35.08 | 56.07 | 38.99 | 61.11 | 102.07 | 64.54 | 2.69 | -1.17 | n/a |
| demand_prop_full_safetyoff | 20 | 33.87 | 33.56 | 30.48 | 37.56 | 61.55 | 59.12 | 61.31 | 2.65 | -1.13 | n/a |
| demand_prop_full_safetyon | 20 | 33.75 | 34.14 | 30.74 | 36.37 | 60.38 | 60.51 | 61.58 | 2.62 | -1.12 | n/a |
| dqn_aug_subsample_safetyoff | 20 | 37.98 | 28.57 | 54.84 | 30.51 | 54.08 | 104.63 | 55.04 | 2.85 | -1.05 | n/a |
| dqn_aug_subsample_safetyon | 20 | 39.26 | 31.67 | 50.28 | 35.83 | 58.78 | 93.92 | 62.09 | 2.68 | -1.13 | n/a |
| dqn_full_safetyoff | 20 | 44.44 | 23.58 | 79.53 | 30.20 | 41.28 | 151.47 | 53.55 | 3.33 | -0.98 | n/a |
| dqn_full_safetyon | 20 | 44.30 | 32.56 | 60.36 | 39.98 | 59.55 | 110.71 | 64.92 | 2.70 | -1.16 | n/a |
| dqn_real_only_safetyoff | 20 | 41.56 | 24.81 | 66.10 | 33.77 | 40.43 | 127.39 | 56.92 | 3.34 | -0.99 | n/a |
| dqn_real_only_safetyon | 20 | 43.79 | 33.94 | 57.37 | 40.06 | 60.42 | 104.74 | 64.98 | 2.69 | -1.16 | n/a |
| equal_split_full_safetyoff | 20 | 52.39 | 30.15 | 28.30 | 98.70 | 58.33 | 55.47 | 188.59 | 2.78 | -2.03 | n/a |
| equal_split_full_safetyon | 20 | 43.16 | 31.96 | 28.98 | 68.55 | 58.95 | 57.34 | 83.26 | 2.62 | -1.25 | n/a |
| no_control_full_safetyoff | 20 | 60.91 | 60.86 | 56.04 | 65.84 | 119.65 | 111.58 | 128.80 | 4.93 | -2.26 | n/a |
| no_control_full_safetyon | 20 | 37.34 | 37.31 | 35.71 | 38.99 | 64.78 | 69.60 | 67.65 | 2.71 | -1.21 | n/a |
| ppo_aug_subsample_safetyoff | 20 | 53.02 | 32.62 | 85.60 | 40.84 | 60.29 | 170.77 | 78.08 | 5.35 | -1.44 | n/a |
| ppo_aug_subsample_safetyon | 20 | 40.86 | 32.47 | 55.16 | 34.97 | 59.69 | 102.18 | 62.08 | 2.67 | -1.14 | n/a |
| ppo_full_safetyoff | 20 | 51.50 | 32.80 | 88.00 | 33.71 | 60.95 | 175.60 | 63.44 | 5.04 | -1.33 | n/a |
| ppo_full_safetyon | 20 | 42.83 | 32.24 | 59.00 | 37.26 | 59.57 | 108.10 | 63.86 | 2.68 | -1.15 | n/a |
| ppo_real_only_safetyoff | 20 | 51.07 | 31.45 | 92.14 | 29.61 | 59.34 | 183.88 | 54.08 | 5.18 | -1.26 | n/a |
| ppo_real_only_safetyon | 20 | 42.23 | 33.46 | 57.58 | 35.64 | 60.17 | 104.10 | 62.53 | 2.67 | -1.14 | n/a |
| ressdhppo_full_safetyoff | 20 | 34.39 | 32.82 | 33.79 | 36.56 | 60.83 | 65.41 | 62.12 | 2.66 | -21.55 | 0.15 |
| ressdhppo_full_safetyon | 20 | 33.81 | 33.71 | 31.07 | 36.65 | 60.18 | 61.07 | 61.96 | 2.62 | -21.32 | 0.14 |
| sdhppo_aug_subsample_safetyoff | 20 | 52.84 | 36.25 | 88.75 | 33.53 | 69.50 | 176.55 | 63.44 | 4.84 | -1.39 | n/a |
| sdhppo_aug_subsample_safetyon | 20 | 43.59 | 33.01 | 59.65 | 38.10 | 61.19 | 109.63 | 66.62 | 2.73 | -1.19 | n/a |
| sdhppo_full_safetyoff | 20 | 51.52 | 33.47 | 85.62 | 35.46 | 61.29 | 170.74 | 67.15 | 4.89 | -1.35 | n/a |
| sdhppo_full_safetyon | 20 | 42.47 | 33.66 | 57.05 | 36.70 | 60.97 | 104.11 | 64.20 | 2.70 | -1.16 | n/a |
| sdhppo_no_dueling_safetyoff | 20 | 53.04 | 33.55 | 89.59 | 35.98 | 61.70 | 178.85 | 67.76 | 5.29 | -1.38 | n/a |
| sdhppo_no_dueling_safetyon | 20 | 43.23 | 34.51 | 56.80 | 38.39 | 63.20 | 102.84 | 65.35 | 2.70 | -1.19 | n/a |
| sdhppo_real_only_safetyoff | 20 | 51.46 | 33.39 | 88.06 | 32.94 | 60.94 | 175.58 | 60.70 | 4.87 | -1.30 | n/a |
| sdhppo_real_only_safetyon | 20 | 43.26 | 35.72 | 56.79 | 37.28 | 64.59 | 102.77 | 66.27 | 2.72 | -1.21 | n/a |
| threshold_full_safetyoff | 20 | 70.01 | 70.30 | 68.73 | 71.00 | 103.18 | 120.07 | 104.82 | 2.78 | -1.81 | n/a |
| threshold_full_safetyon | 20 | 68.90 | 70.56 | 65.00 | 71.15 | 103.32 | 117.05 | 104.84 | 2.78 | -1.81 | n/a |

## Skenario non-stasioner (eksploratif)

| cell | n | viol_total | scen_diurnal | scen_flash |
|---|---|---|---|---|
| bcsdhppo_full_safetyoff | 20 | 36.87 | 51.39 | 41.83 |
| bcsdhppo_full_safetyon | 20 | 33.79 | 50.51 | 43.33 |
| ddqn_aug_subsample_safetyoff | 20 | 38.48 | 40.79 | 41.19 |
| ddqn_aug_subsample_safetyon | 20 | 39.28 | 48.94 | 45.09 |
| ddqn_full_safetyoff | 20 | 45.95 | 47.42 | 49.68 |
| ddqn_full_safetyon | 20 | 44.05 | 52.18 | 51.74 |
| ddqn_real_only_safetyoff | 20 | 43.13 | 52.48 | 48.38 |
| ddqn_real_only_safetyon | 20 | 43.38 | 56.12 | 51.85 |
| demand_prop_full_safetyoff | 20 | 33.87 | 53.42 | 37.98 |
| demand_prop_full_safetyon | 20 | 33.75 | 50.80 | 44.22 |
| dqn_aug_subsample_safetyoff | 20 | 37.98 | 40.48 | 39.78 |
| dqn_aug_subsample_safetyon | 20 | 39.26 | 49.37 | 45.19 |
| dqn_full_safetyoff | 20 | 44.44 | 45.23 | 47.99 |
| dqn_full_safetyon | 20 | 44.30 | 51.47 | 51.39 |
| dqn_real_only_safetyoff | 20 | 41.56 | 52.31 | 46.15 |
| dqn_real_only_safetyon | 20 | 43.79 | 55.69 | 51.88 |
| equal_split_full_safetyoff | 20 | 52.39 | 52.60 | 56.70 |
| equal_split_full_safetyon | 20 | 43.16 | 51.21 | 51.07 |
| no_control_full_safetyoff | 20 | 60.91 | 61.25 | 64.82 |
| no_control_full_safetyon | 20 | 37.34 | 50.20 | 46.95 |
| ppo_aug_subsample_safetyoff | 20 | 53.02 | 55.57 | 54.84 |
| ppo_aug_subsample_safetyon | 20 | 40.86 | 51.46 | 48.89 |
| ppo_full_safetyoff | 20 | 51.50 | 54.55 | 53.36 |
| ppo_full_safetyon | 20 | 42.83 | 52.61 | 50.89 |
| ppo_real_only_safetyoff | 20 | 51.07 | 54.90 | 53.77 |
| ppo_real_only_safetyon | 20 | 42.23 | 52.98 | 50.58 |
| ressdhppo_full_safetyoff | 20 | 34.39 | 53.37 | 38.42 |
| ressdhppo_full_safetyon | 20 | 33.81 | 51.01 | 43.80 |
| sdhppo_aug_subsample_safetyoff | 20 | 52.84 | 54.55 | 54.47 |
| sdhppo_aug_subsample_safetyon | 20 | 43.59 | 52.74 | 50.30 |
| sdhppo_full_safetyoff | 20 | 51.52 | 53.65 | 53.34 |
| sdhppo_full_safetyon | 20 | 42.47 | 53.00 | 49.69 |
| sdhppo_no_dueling_safetyoff | 20 | 53.04 | 55.69 | 54.45 |
| sdhppo_no_dueling_safetyon | 20 | 43.23 | 53.40 | 51.15 |
| sdhppo_real_only_safetyoff | 20 | 51.46 | 54.72 | 52.94 |
| sdhppo_real_only_safetyon | 20 | 43.26 | 54.02 | 51.31 |
| threshold_full_safetyoff | 20 | 70.01 | 74.76 | 74.56 |
| threshold_full_safetyon | 20 | 68.90 | 73.75 | 73.70 |

## Sensitivitas ambang SLA (eksploratif; kebijakan dilatih pada 6/70/7)

| cell | viol_total | sens_0.5x | sens_0.75x | sens_1.5x | sens_2x | sens_real_train_median |
|---|---|---|---|---|---|---|
| bcsdhppo_full_safetyoff | 36.88 | 38.52 | 37.47 | 35.73 | 34.70 | 40.08 |
| bcsdhppo_full_safetyon | 33.79 | 35.78 | 34.61 | 32.55 | 31.66 | 37.70 |
| ddqn_aug_subsample_safetyoff | 38.48 | 40.41 | 39.34 | 36.90 | 35.55 | 41.64 |
| ddqn_aug_subsample_safetyon | 39.28 | 41.53 | 40.37 | 37.33 | 35.68 | 43.12 |
| ddqn_full_safetyoff | 45.95 | 46.77 | 46.37 | 45.05 | 44.02 | 47.12 |
| ddqn_full_safetyon | 44.05 | 46.94 | 45.49 | 41.39 | 38.99 | 48.60 |
| ddqn_real_only_safetyoff | 43.13 | 44.61 | 43.86 | 41.68 | 40.38 | 45.34 |
| ddqn_real_only_safetyon | 43.38 | 46.28 | 44.80 | 40.63 | 38.36 | 48.00 |
| demand_prop_full_safetyoff | 33.87 | 34.27 | 34.01 | 33.14 | 32.46 | 34.81 |
| demand_prop_full_safetyon | 33.75 | 34.83 | 34.41 | 33.04 | 32.42 | 35.37 |
| dqn_aug_subsample_safetyoff | 37.98 | 39.99 | 38.89 | 36.39 | 35.11 | 41.46 |
| dqn_aug_subsample_safetyon | 39.26 | 41.34 | 40.27 | 37.41 | 35.81 | 42.83 |
| dqn_full_safetyoff | 44.44 | 45.67 | 45.03 | 43.06 | 41.47 | 46.29 |
| dqn_full_safetyon | 44.30 | 47.09 | 45.71 | 41.79 | 39.42 | 48.73 |
| dqn_real_only_safetyoff | 41.56 | 43.32 | 42.41 | 40.07 | 38.79 | 44.34 |
| dqn_real_only_safetyon | 43.79 | 46.59 | 45.16 | 41.12 | 38.84 | 48.32 |
| equal_split_full_safetyoff | 52.39 | 52.70 | 52.43 | 52.10 | 51.77 | 52.74 |
| equal_split_full_safetyon | 43.16 | 43.86 | 43.48 | 42.32 | 41.38 | 44.18 |
| no_control_full_safetyoff | 60.91 | 61.09 | 61.01 | 60.75 | 60.62 | 61.16 |
| no_control_full_safetyon | 37.34 | 39.19 | 38.21 | 36.08 | 35.27 | 40.72 |
| ppo_aug_subsample_safetyoff | 53.02 | 53.28 | 53.14 | 52.84 | 52.66 | 53.41 |
| ppo_aug_subsample_safetyon | 40.86 | 44.35 | 42.55 | 38.16 | 36.18 | 46.79 |
| ppo_full_safetyoff | 51.50 | 51.64 | 51.56 | 51.36 | 51.22 | 51.61 |
| ppo_full_safetyon | 42.83 | 46.47 | 44.58 | 39.92 | 37.51 | 48.98 |
| ppo_real_only_safetyoff | 51.07 | 51.30 | 51.17 | 50.91 | 50.73 | 51.32 |
| ppo_real_only_safetyon | 42.23 | 46.04 | 44.11 | 38.92 | 36.42 | 48.46 |
| ressdhppo_full_safetyoff | 34.39 | 35.19 | 34.74 | 33.74 | 33.09 | 35.73 |
| ressdhppo_full_safetyon | 33.81 | 35.21 | 34.42 | 32.92 | 32.31 | 35.91 |
| sdhppo_aug_subsample_safetyoff | 52.85 | 53.10 | 52.96 | 52.62 | 52.41 | 53.13 |
| sdhppo_aug_subsample_safetyon | 43.58 | 46.44 | 45.01 | 40.93 | 38.80 | 48.40 |
| sdhppo_full_safetyoff | 51.52 | 51.68 | 51.60 | 51.34 | 51.17 | 51.70 |
| sdhppo_full_safetyon | 42.47 | 46.11 | 44.22 | 39.43 | 37.10 | 48.48 |
| sdhppo_no_dueling_safetyoff | 53.04 | 53.15 | 53.11 | 52.91 | 52.75 | 53.15 |
| sdhppo_no_dueling_safetyon | 43.23 | 46.84 | 45.01 | 40.06 | 37.48 | 49.36 |
| sdhppo_real_only_safetyoff | 51.46 | 51.64 | 51.55 | 51.30 | 51.11 | 51.65 |
| sdhppo_real_only_safetyon | 43.26 | 47.08 | 45.12 | 40.01 | 37.47 | 49.59 |
| threshold_full_safetyoff | 70.01 | 74.00 | 72.15 | 65.65 | 61.93 | 75.72 |
| threshold_full_safetyon | 68.90 | 72.48 | 70.67 | 65.45 | 62.57 | 74.14 |
