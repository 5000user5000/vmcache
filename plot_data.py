import matplotlib.pyplot as plt
import pandas as pd
import sys

def plot_data(input_file_name, output_file_name):
    # 讀取數據
    data = pd.read_csv(input_file_name, header=None, names=['tx', 'rmb', 'wmb'])

    # 為tx, rmb, wmb 繪圖
    for column in data.columns:
        plt.figure()
        plt.plot(data[column])
        base_name = output_file_name.split('.')[0]
        plt.title(f"{base_name}: {column}")
        plt.xlabel('Index')
        plt.ylabel(column)
        plt.savefig(output_file_name)  # 儲存圖片
        plt.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('argument: input_file_name output_file_name')
        sys.exit()

    plot_data(sys.argv[0], sys.argv[1])

