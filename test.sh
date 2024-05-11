#!/bin/bash

# 定義輸出文件
output_file="output.txt"
result_rnd_file="result_rnd.txt"
result_file="result.txt"

# 定義參數的範圍和步長
start=5
end=85
step=20

# 清空現有的輸出文件
> "$result_rnd_file"
> "$result_file"

echo "Starting RNDREAD tests..."
for (( i=$start; i<=$end; i+=$step ))
do
    echo "Running RNDREAD program with parameter: $i"
    # 清空現有的輸出文件
    > "$output_file"
    # 執行C++程序並將輸出追加到 output_file
    sudo BLOCK=/dev/loop0 THREADS=4 DATASIZE=$i RNDREAD=1 ./vmcache >> "$output_file"
    echo "Waiting for operation to settle..."
    sleep 2  # Adds a 2-second delay to ensure file operations complete
    # 調用Python腳本處理數據
    python test_analysis.py "$output_file" "$result_rnd_file"
    echo "Completed RNDREAD for parameter: $i"
done

echo "Starting standard tests..."
for (( i=$start; i<=$end; i+=$step ))
do
    echo "Running standard program with parameter: $i"
    > "$output_file"
    sudo BLOCK=/dev/loop0 THREADS=4 DATASIZE=$i ./vmcache >> "$output_file"
    sleep 2  # Adds a delay
    python test_analysis.py "$output_file" "$result_file"
    echo "Completed standard test for parameter: $i"
done

echo "程序執行完成，結果已保存到 $result_rnd_file 和 $result_file ！"
