import os
import glob
import matplotlib.pyplot as plt
import numpy as np

# Function to read data from a text file
def read_data(file_path, skip_foot):
    ts,tx,rmb,wmb,system,threads,datasize,workload,batch = np.genfromtxt(file_path, skip_header=3, skip_footer=skip_foot, delimiter=',', unpack=True)
    return tx, rmb, wmb

def plot_data(type, file_name, data_sizes, value1, value2, label1, label2):
    # Plotting the data
    plt.figure()

    plt.plot(data_sizes, value1, label=label1, color='blue')
    plt.plot(data_sizes, value2, label=label2, color='red')

    # Adding labels and title
    plt.xlabel('data size')
    plt.ylabel(file_name)
    plt.title(type)
    plt.legend()
    plt.grid(True)

    # Create output directory if it doesn't exist
    output_dir = './pic'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.savefig(f"{output_dir}//{type}_{file_name}_comparison.png")
    plt.close()


def main(plot_type, base_folder_path):

    # Get list of all text files in the mutex and ori folders
    mutex_files = sorted(glob.glob(os.path.join(base_folder_path, 'mutex', 'dsize_*.txt')))
    ori_files = sorted(glob.glob(os.path.join(base_folder_path, 'ori', 'dsize_*.txt')))

    # Dictionary to store the data from each file
    mutex_data = {}
    ori_data = {}

    # Read data from each mutex file
    for file_path in mutex_files:
        if plot_type=='rnd':
            mutex_data[file_path] = read_data(file_path, skip_foot=0)
        else:
            mutex_data[file_path] = read_data(file_path, skip_foot=1)

    # Read data from each ori file
    for file_path in ori_files:
        if plot_type=='rnd':
            ori_data[file_path] = read_data(file_path, skip_foot=0)
        else:
            ori_data[file_path] = read_data(file_path, skip_foot=1)

    # Extract data sizes from file names for x-axis
    data_sizes = [int(os.path.basename(file).split('_')[1].split('.')[0]) for file in mutex_files]

    mutex_tx_values, mutex_rmb_values, mutex_wmb_values = [], [], []
    ori_tx_values, ori_rmb_values, ori_wmb_values =  [], [], []

    for mutex_file, ori_file in zip(mutex_files, ori_files):

        mutex_tx, mutex_rmb, mutex_wmb = mutex_data[mutex_file]
        ori_tx, ori_rmb, ori_wmb = ori_data[ori_file]

        mutex_tx_values.append(np.mean(mutex_tx))
        ori_tx_values.append(np.mean(ori_tx))

        mutex_rmb_values.append(np.mean(mutex_rmb))
        ori_rmb_values.append(np.mean(ori_rmb))

        mutex_wmb_values.append(np.mean(mutex_wmb))
        ori_wmb_values.append(np.mean(ori_wmb))

    plot_data(plot_type, 'tx', data_sizes, mutex_tx_values, ori_tx_values, label1='Mutex', label2='Original')
    plot_data(plot_type, 'rmb', data_sizes, mutex_rmb_values, ori_rmb_values, label1='Mutex', label2='Original')
    plot_data(plot_type, 'wmb', data_sizes, mutex_wmb_values, ori_wmb_values, label1='Mutex', label2='Original')

    

if __name__ == '__main__':

    main('tpcc', './data/tpcc/')

    main('rnd', './data/rnd/')
