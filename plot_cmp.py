import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_multiple_data(files, title, labels):
    # 讀取數據
    data = [pd.read_csv(file, header=None, names=['tx', 'rmb', 'wmb']) for file in files]
    x_ticks = np.linspace(5, 85, len(data[0]))  # 設定是取 data size 5~85的數據

    colors = ['red', 'blue', 'green', 'orange', 'purple', 'black']
    markers = ['o', 'x', 's', 'd', '^', 'v']
    linestyles = ['-', '--', '-.', ':', '-', '--']

    # 為 tx, rmb, wmb 繪圖
    for column in data[0].columns:
        fig, axes = plt.subplots(3, 2, figsize=(15, 10), sharex=True, sharey=True)
        axes = axes.flatten()
        
        for i in range(1, len(data)):
            ax = axes[i-1]
            ax.plot(x_ticks, data[0][column], label='Original', color=colors[0], marker=markers[0], linestyle=linestyles[0])
            ax.plot(x_ticks, data[i][column], label=labels[i], color=colors[i], marker=markers[i], linestyle=linestyles[i])
            ax.set_title(f"{labels[i]} vs Original")
            ax.set_xlabel('Data Size')
            ax.set_ylabel(column)
            ax.legend()
            ax.grid(True)

        plt.suptitle(f"{title}: {column}")
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(f"./pic/{title}_{column}_comparison.png")  # 儲存圖片
        plt.close()

if __name__ == '__main__':
    plot_multiple_data(
        ['./data/result_rnd_o.txt', './data/result_rnd_m.txt', './data/result_rnd_me.txt', './data/result_rnd_f.txt', './data/result_rnd_y.txt', './data/result_rnd_bm.txt'], 
        'Random Lookup', 
        ['Original', 'Mutex', 'Merge', 'Futex', 'Yield-Opt', 'Bitmap']
    )
    
    plot_multiple_data(
        ['./data/result_o.txt', './data/result_m.txt', './data/result_me.txt', './data/result_f.txt', './data/result_y.txt', './data/result_bm.txt'], 
        'TPC-C', 
        ['Original', 'Mutex', 'Merge', 'Futex', 'Yield-Opt', 'Bitmap']
    )
