import time, os, json

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
input_file_path = "/Users/alicewish/我的坚果云/Timing Export筛选.csv"
output_file_path = "/Users/alicewish/我的坚果云/Timing Export筛选GBK.csv"

# ================按行读取输入文本================
print("开始读取")
read_text = open(input_file_path, 'r').read()  # 读取文本

# ================写入文本================

f = open(output_file_path, 'wb')
try:
    f.write(read_text.encode('gbk','ignore'))
finally:
    f.close()
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
