import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

def plot_data(file_name, title):
    # 讀取數據
    data = pd.read_csv(file_name, header=None, names=['tx', 'rmb', 'wmb'])
    x_ticks = np.linspace(5, 85, len(data)) # 設定是取 data size 5~85的數據
    # 為tx, rmb, wmb 繪圖
    for column in data.columns:
        plt.figure()
        plt.plot(x_ticks, data[column])
        plt.title(f"{title}: {column}")
        plt.xlabel('data size')
        plt.ylabel(column)
        
        plt.savefig(f"{title}_{column}.png")  # 儲存圖片
        plt.close()

if __name__ == '__main__':
    # 繪製 r1.txt 的圖
    plot_data('result_rnd.txt', 'Random Lookup')

    # 繪製 r2.txt 的圖
    plot_data('result.txt', 'TPC-C')
