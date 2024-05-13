import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import sys

def plot_data(input_file_name, output_file_name):
    # 讀取數據
    try:
        data = pd.read_csv(input_file_name, header=None, names=['tx', 'rmb', 'wmb'], on_bad_lines='skip')
    except Exception as e:
        print(f"Failed to read the data file: {e}")
        return
    
    x_ticks = np.linspace(5, 85, len(data)) # 設定是取 data size 5~85的數據
    # 為tx, rmb, wmb 繪圖
    for column in data.columns:
        plt.figure()
        plt.plot(x_ticks, data[column])
        base_name = output_file_name.split('.')[0]
        plt.title(f"{base_name}: {column}")
        plt.xlabel('data size')
        plt.ylabel(column)
        
        plt.savefig(f"{base_name}: {column}")  # 儲存圖片
        plt.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('argument: input_file_name output_file_name')
        sys.exit()

    plot_data(sys.argv[1], sys.argv[2])

