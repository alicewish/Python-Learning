from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()

# ================正则匹配================
pattern = re.compile(r'http://ww2.sinaimg.cn/large/[^)]*')
# 匹配http://ww2.sinaimg.cn/large/a15b4afegw1f52rdah5gfj21hk1564hc

# ================使用Pattern匹配文本，获得全部匹配结果================
find = pattern.findall(read_text)  # 列表形式存储的结果
info_line = []
for i in range(len(find)):
    full_html = '<img src="' + find[i] + '" />'
    info_line.append(full_html)
info = "\r\n".join(info_line)
print(info)
print(len(find))


# ================写入剪贴板================
import pyperclip

pyperclip.copy(info)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
