import json

path = "/home/habb/Kuliah/sdn-iot/Reinforcement Learning/revision/allModel4.ipynb"
with open(path, "r") as f:
    nb = json.load(f)

# Update cell 4 (convergence plot)
source4 = "".join(nb["cells"][4]["source"])
csv_code4 = """import pandas as pd
for name in training_results:
    df_train = pd.DataFrame({
        'Epoch': range(1, len(training_results[name]['loss']) + 1),
        'Loss': training_results[name]['loss'],
        'Reward': training_results[name]['reward']
    })
    df_train.to_csv(f'training_convergence_{name.replace(" ","_")}.csv', index=False)

"""
if "training_convergence_" not in source4:
    # Insert right before the plotting loop
    source4 = source4.replace("for name in training_results:\n    plt.figure", csv_code4 + "for name in training_results:\n    plt.figure")
    nb["cells"][4]["source"] = source4.splitlines(True)


# Update cell 10 (delay tracking plot)
source10 = "".join(nb["cells"][10]["source"])
# We need to inject df_delay_plot = pd.DataFrame() before the inner loop
# And df_delay_plot[m] = data_viz inside the loop
# And df_delay_plot.to_csv(...) after the inner loop

old_outer_loop = "for p_label, sla_val, col_name, sub_idx in port_configs:\n    plt.subplot(3, 1, sub_idx)\n    for m in models_to_plot:"
new_outer_loop = "for p_label, sla_val, col_name, sub_idx in port_configs:\n    df_delay_plot = pd.DataFrame()\n    plt.subplot(3, 1, sub_idx)\n    for m in models_to_plot:"
source10 = source10.replace(old_outer_loop, new_outer_loop)

old_data_viz = "data_viz = data_viz + 0.6 \n            # -----------------------------\n            \n            plt.plot"
new_data_viz = "data_viz = data_viz + 0.6 \n            # -----------------------------\n            \n            df_delay_plot[m] = data_viz\n            \n            plt.plot"
source10 = source10.replace(old_data_viz, new_data_viz)

old_except = "        except FileNotFoundError:\n            pass\n            \n    plt.axhline"
new_except = "        except FileNotFoundError:\n            pass\n            \n    df_delay_plot.to_csv(f'delay_tracking_plot_{col_name}.csv', index=False)\n    \n    plt.axhline"
source10 = source10.replace(old_except, new_except)

nb["cells"][10]["source"] = source10.splitlines(True)

with open(path, "w") as f:
    json.dump(nb, f, indent=1)

print("Added CSV generation to plotting cells.")
