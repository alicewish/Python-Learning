from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
refer_file_path = "/Users/alicewish/我的坚果云/图床.txt"  # 词典文件的地址

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()

print(read_text)
f = open("/Users/alicewish/我的坚果云/图床.txt", 'w')
try:
    f.write(read_text)
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
