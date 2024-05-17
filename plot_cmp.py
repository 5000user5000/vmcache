import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 


def plot_data(file1, file2, file3, file4, file5, title,labal1,label2,label3,label4,label5):
    # 讀取數據
    data1 = pd.read_csv(file1, header=None, names=['tx', 'rmb', 'wmb'])
    data2 = pd.read_csv(file2, header=None, names=['tx', 'rmb', 'wmb'])
    data3 = pd.read_csv(file3, header=None, names=['tx', 'rmb', 'wmb'])
    data4 = pd.read_csv(file4, header=None, names=['tx', 'rmb', 'wmb'])
    data5 = pd.read_csv(file5, header=None, names=['tx', 'rmb', 'wmb'])
    x_ticks = np.linspace(5, 85, len(data1)) # 設定是取 data size 5~85的數據
    # 為tx, rmb, wmb 繪圖
    for column in data1.columns:
        plt.figure()
        plt.plot(x_ticks, data1[column], label=labal1 ,color='red')
        plt.plot(x_ticks, data2[column], label=label2, color='blue')
        plt.plot(x_ticks, data3[column], label=label3, color='green')
        plt.plot(x_ticks, data4[column], label=label4, color='orange')
        plt.plot(x_ticks, data5[column], label=label5, color='purple')
        plt.title(f"{title}: {column}")
        plt.xlabel('data size')
        plt.ylabel(column)
        plt.legend(title='Legend', loc='upper right')

        plt.savefig(f"./pic/{title}_{column}_comparison.png")  # 儲存圖片
        plt.close()

def plot_multiple_data(files, title, labels):
    # 讀取數據
    data = [pd.read_csv(file, header=None, names=['tx', 'rmb', 'wmb']) for file in files]
    x_ticks = np.linspace(5, 85, len(data[0]))  # 設定是取 data size 5~85的數據

    colors = ['red', 'blue', 'green', 'orange', 'purple']
    markers = ['o', 'x', 's', 'd', '^']
    linestyles = ['-', '--', '-.', ':', '-']

    # 為 tx, rmb, wmb 繪圖
    for column in data[0].columns:
        plt.figure(figsize=(12, 8))
        for i in range(len(data)):
            plt.plot(x_ticks, data[i][column], label=labels[i], color=colors[i], marker=markers[i], linestyle=linestyles[i])
        plt.title(f"{title}: {column}")
        plt.xlabel('data size')
        plt.ylabel(column)
        plt.legend(title='Legend', loc='upper right')

        plt.grid(True)
        plt.savefig(f"./pic/{title}_{column}_comparison.png")  # 儲存圖片
        plt.close()

if __name__ == '__main__':

    plot_multiple_data(['./data/result_rnd_o.txt', './data/result_rnd_m.txt', './data/result_rnd_mm.txt', './data/result_rnd_f.txt', './data/result_rnd_y.txt'], 
                       'Random Lookup', 
                       ['Original', 'Mutex', 'Mutex + Merge', 'Futex', 'Yield-Opt'])
    
    plot_multiple_data(['./data/result_o.txt', './data/result_m.txt', './data/result_mm.txt', './data/result_f.txt', './data/result_y.txt'], 
                       'TPC-C', 
                       ['Original', 'Mutex', 'Mutex + Merge', 'Futex', 'Yield-Opt'])
