import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

def plot_data(file1, file2, title,labal1,label2):
    # 讀取數據
    data1 = pd.read_csv(file1, header=None, names=['tx', 'rmb', 'wmb'])
    data2 = pd.read_csv(file2, header=None, names=['tx', 'rmb', 'wmb'])
    x_ticks = np.linspace(5, 85, len(data1)) # 設定是取 data size 5~85的數據
    # 為tx, rmb, wmb 繪圖
    for column in data1.columns:
        plt.figure()
        plt.plot(x_ticks, data1[column], label=labal1 ,color='blue')  # 繪製第一筆數據
        plt.plot(x_ticks, data2[column], label=label2, color='red')  # 繪製第二筆數據，使用紅線
        plt.title(f"{title}: {column}")
        plt.xlabel('data size')
        plt.ylabel(column)
        plt.legend(title='Legend', loc='upper left')  # 加上圖標，並指定位置
        
        plt.savefig(f"./pic/{title}_{column}_comparison.png")  # 儲存圖片
        plt.close()

if __name__ == '__main__':
    plot_data('./data/result_rnd_mutex.txt', './data/result_rnd_ori.txt', 'Random Lookup', 'Mutex', 'Original')
    plot_data('./data/result_mutex.txt', './data/result_ori.txt', 'TPC-C', 'Mutex', 'Original')
