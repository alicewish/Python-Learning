from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()

read_text_line = read_text.splitlines()
out_text_line = []
for i in range(len(read_text_line)):
    if "#" in read_text_line[i] and len(read_text_line[i]) < 50:
        out_text_line.append("### " + read_text_line[i])
    else:
        out_text_line.append(read_text_line[i])

out_text = "\r\n".join(out_text_line)
print(out_text)
# ================写入剪贴板================
import pyperclip

pyperclip.copy(out_text)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
