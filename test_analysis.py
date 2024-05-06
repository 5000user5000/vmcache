# 資料格式 ts,tx,rmb,wmb,system,threads,datasize,workload,batch
# 讀取 tx
import sys

def read_data(input_file,output_file):
    tx_data = []
    rmb_data = []
    wmb_data = []
    with open(input_file, 'r', encoding='utf-8') as file:
        next(file)  # 跳過第一行
        for line in file:
            columns = line.strip().split(',')
            if len(columns) > 1:  # 確保有第二個元素
                # print(columns[1])  # 輸出第二個元素
                tx_data.append(columns[1])
                rmb_data.append(columns[2])
                wmb_data.append(columns[3])
    # 將字串轉換為浮點數
    tx_data = list(map(float, tx_data))
    rmb_data = list(map(float, rmb_data))
    wmb_data = list(map(float, wmb_data))
    # 將平均值資料以添加方式寫入檔案，(tx, rmb, wmb)
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(str(round(sum(tx_data) / len(tx_data), 2)) + ',' + str(round(sum(rmb_data) / len(rmb_data), 2)) + ',' + str(round(sum(wmb_data) / len(wmb_data), 2)) + '\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python test.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        read_data(input_file,output_file)