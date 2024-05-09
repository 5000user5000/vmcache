import matplotlib.pyplot as plt
import pandas as pd

def plot_data(file_name, title):
    # 讀取數據
    data = pd.read_csv(file_name, header=None, names=['tx', 'rmb', 'wmb'])

    # 為tx, rmb, wmb 繪圖
    for column in data.columns:
        plt.figure()
        plt.plot(data[column])
        plt.title(f"{title}: {column}")
        plt.xlabel('Index')
        plt.ylabel(column)
        plt.savefig(f"{title}_{column}.png")  # 儲存圖片
        plt.close()

if __name__ == '__main__':
    # 繪製 r1.txt 的圖
    plot_data('result_rnd.txt', 'Random Lookup')

    # 繪製 r2.txt 的圖
    plot_data('result.txt', 'TPC-C')
