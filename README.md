# vmcache

For a detailed introduction, please refer to the original author's code [vmcache](https://github.com/viktorleis/vmcache). This document focuses on our modifications.

## Code Overview

vmcache is an implementation of an efficient buffer manager and B-tree data structure designed for managing and accessing large-scale data. The programs in the `./src` directory are based on the original version but have been modified in various ways to enhance the performance of vmcache. The modifications include bitmap, futex, merge, mutex, and yopt approaches. Besides completing the author's TODOs, the aim is to improve the overall efficiency of vmcache.

Contributions: bitmap by **TENG, YA-WEN** , mutex_opt by **WU, CHI-CHIA** , mutex + futex + merge + yopt by **CHOU,CHE-WEI**.

- **bitmap**: Implements free space management for storage.
- **mutex** : Handle mutual exclusion locks.
- **mutex_opt** : Optimizes mutual exclusion locks using `lock_guard` , `unique_lock`, and finer-grained locking mechanisms for better performance and reduced contention.
- **futex** : Utilizes fast userspace mutexes to minimize lock overhead and improve efficiency
- **merge**: Completes the unfinished B-tree inner node merge by the original author.
- **yopt**: Dynamically adjusts the waiting strategy of the original spinlock based on the duration.

Additional files:

- `colab_example.ipynb`: An example of how to execute the program, intended to be run on Google Colab.
- `test.sh`: A script for automated testing.
- `test_analysis.py`: Calculates the average from each program execution's output and writes the results to a file.
- `plot_data.py`: Visualizes the data from the results file.
- `plot_cmp.py`: Compares multiple data sets using line charts, with results available in `./pic`.
- `plot_cmp_sub.py`: Creates five subplots to compare each of the five methods with the original implementation for clearer presentation, with results available in `./pic_sub`.
- `eff_cmp.py` is used to compare the overall performance of different methods with the original version. The method used here involves summing the tx (transaction rate), rmb (read memory bandwidth), and wmb (write memory bandwidth) across all data sizes, in order to evaluate the overall performance improvement of various methods.

## Comparison Data

- **tx**: Transaction throughput.
- **rmb** and **wmb**: Read and write throughput, respectively.
- **Data size**: Ranges from 5 to 85, in increments of 5.
- **Benchmarks**: Includes Random read benchmark and TPC-C.

There are six data sets in total, including the original version. All data sets are presented in a line chart available in `./pic`. Comparisons between each method and the original version are available in `./pic_sub`.

## Environment

The code is executed using Google Colab. For detailed instructions, please refer to `colab_example.ipynb`. The code requires an environment running Ubuntu 22.04 or later, with GCC version 10.0 or higher. The program uses a Loop Device to simulate storage access.

- **Colab CPU**: Intel(R) Xeon(R) CPU @ 2.20GHz, 2 cores, 4 threads.

**Note**: When running `test.sh`, if the data size exceeds 30, a `structure needs cleaning` issue might occur. In such cases, you must manually execute the commands one by one.

## Result

### Random Lookup Improvements

```
                 tx        rmb        wmb
Mutex     -2.639638       NaN        NaN
Mutex-Opt  5.258519       NaN        NaN
Merge     -2.350825       NaN        NaN
Futex      6.683135       NaN        NaN
Yield-Opt  3.078284       NaN        NaN
Bitmap     0.302605       NaN        NaN
```

- **Mutex**: Decrease in transaction rate by approximately 2.64%.
- **Mutex-Opt**: Increase in transaction rate by approximately 5.26%.
- **Merge**: Decrease in transaction rate by approximately 2.35%.
- **Futex**: Increase in transaction rate by approximately 6.68%.
- **Yield-Opt**: Increase in transaction rate by approximately 3.08%.
- **Bitmap**: Increase in transaction rate by approximately 0.30%.

### TPC-C Improvements

```
                  tx        rmb        wmb
Mutex     -33.948303 -26.150875 -29.334250
Merge     -12.234084  42.911946  30.710619
Futex      -0.503327  32.595263  25.583087
Yield-Opt -13.376186  16.624614  11.445491
Bitmap      4.193579  26.815139  24.230971
```

- **Mutex**: Shows a significant decrease in tx, rmb, and wmb by approximately 33.95%, 26.15%, and 29.33% respectively.
- **Merge**: Shows a decrease in transaction rate by approximately 12.23%, but an increase in rmb and wmb by approximately 42.91% and 30.71% respectively.
- **Futex**: Shows a marginal decrease in transaction rate by approximately 0.50%, but an increase in rmb and wmb by approximately 32.60% and 25.58% respectively.
- **Yield-Opt**: Shows a decrease in transaction rate by approximately 13.38%, but an increase in rmb and wmb by approximately 16.62% and 11.45% respectively.
- **Bitmap**: Shows an increase in all metrics: tx by approximately 4.19%, rmb by approximately 26.82%, and wmb by approximately 24.23%.

By using `eff_cmp.py`, you can comprehensively evaluate the performance improvements of various methods over the original implementation, aiding in the selection of the most efficient optimization strategies.
