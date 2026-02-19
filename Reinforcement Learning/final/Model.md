# Reinforcement Learning Final Project Documentation

## 1. Overview
This directory contains the final resources for the Reinforcement Learning-based SDN-IoT traffic optimization research. The contents include the original and augmented datasets, preprocessing pipelines, and the Jupyter notebooks used for Deep Reinforcement Learning (DRL) model training, comparison, and visualization.

## 2. File Descriptions

### Datasets
*   **`dataset_dqn_rich.csv`**: 
    The original, real-world traffic dataset collected from the SDN-IoT network environment. It represents the ground truth and serves as the baseline for initial analysis and model validation.

*   **`eo_wgan_synthetic_data.csv` (Standard Version)**: 
    A synthetic dataset generated using the standard **Hybrid SMOTE + WGAN-GP** methodology. This dataset was designed to expand the feature space into new areas, specifically targeting burst and overload scenarios, though it lacks strict semantic constraints found in the final version.

*   **`synthetic_15k_complete_final.csv` (Final Version)**: 
    The definitive augmented dataset containing 15,000 samples. It is generated using the improved **EO-WGAN + Semantic Constraints + Overlap Logic** approach. This version ensures rigorous adherence to network protocols and realistic traffic constraints (e.g., utilization limits).

*   **`drl_preprocessed_final.csv`**: 
    The final preprocessed dataset formatted specifically for DRL agent training. It includes the necessary State (`state`), Action (`action`), Reward (`reward`), and Next State (`next_state`) tuples derived from the traffic data.

### Notebooks
*   **`DataAugmentation.ipynb`**: 
    Implements the generative models used to create the synthetic data. It contains the code for both the baseline WGAN-GP and the final EO-WGAN with semantic constraints.
    
*   **`Preprocessing.ipynb`**: 
    Handles data cleaning, normalization, and feature engineering. This script transforms raw network logs into the structured format required for the DRL models.

*   **`allModel.ipynb`**: 
    The central experiment notebook. It performs:
    *   Training of various DRL agents (DQN, Double DQN, PPO, SDH-PPO).
    *   Comparative analysis of model performance.
    *   Generation of visualization metrics such as delay tracking and reward convergence.

### Outputs & Visualizations
*   **`sla_violation_report.csv`**: A summary report quantifying the Service Level Agreement (SLA) violation rates for each tested algorithm.
*   **`*.png`** (e.g., `final_delay_tracking.png`, `visual_evaluation.png`): Visual outputs generated during the evaluation phase, illustrating model performance regarding delay minimization and traffic handling.

## 3. Methodology Comparison: Standard vs. Final

The table below outlines the evolution from the standard synthetic data generation approach to the final methodology used for `synthetic_15k_complete_final.csv`.

| Feature | `eo_wgan` (Standard Version) | `synthetic_15k_complete` (Final Version) |
| :--- | :--- | :--- |
| **Core Methodology** | Hybrid SMOTE + WGAN-GP. | **EO-WGAN + Semantic Constraints + Overlap Logic.** |
| **Data Distribution** | Focuses primarily on expanding into new areas (e.g., burst/overload). | Incorporates **Normal Data** (overlaying original traffic) alongside Anomaly Expansions. |
| **Port 4 Logic** | Priority levels may randomly appear as `0`. | **Locked**: Port 4 is strictly constrained to never have `0` priority. |
| **Physical Accuracy** | Feature correlations (e.g., Mbps vs. PPS) are learned purely by the model. | Feature relationships are forced to comply with protocol rules (**Graph-Conditioned**). |
| **Packet Drop Logic** | Drops may appear stochastically due to the generative nature. | Drops occur **only** if utilization exceeds 100% or during specific burst events. |

## 4. Usage Instructions
1.  **Data Generation**: Execute `DataAugmentation.ipynb` to reproduce or extend the synthetic datasets.
2.  **Preprocessing**: Run `Preprocessing.ipynb` to clean raw data and update `drl_preprocessed_final.csv`.
3.  **Experimentation**: Use `allModel.ipynb` to train agents and generate performance reports using the preprocessed data.
