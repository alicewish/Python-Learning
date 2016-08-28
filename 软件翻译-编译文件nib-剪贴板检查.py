import time, re

start_time = time.time()  # 初始时间戳

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()
text_readline = read_text.splitlines()

# ================按行读取输入文本================
output_readline = []  # 初始化按行存储数据列表,不接受换行符

count_left = 0
count_right = 0

for i in range(len(text_readline)):
    if "<string>" in text_readline[i]:
        count_left += 1
    if "</string>" in text_readline[i]:
        count_right += 1
    if count_left != count_right:
        print(i)
        count_left = 0
        count_right = 0

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
