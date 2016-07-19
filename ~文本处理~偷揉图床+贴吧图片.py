from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()

check_set = set()  # 初始化为空集合

info_line = []
if "sinaimg.cn/large/" in read_text:
    # ================正则匹配================
    pattern = re.compile(r'http://ww[0-9].sinaimg.cn/large/[^)"]*')
    # 匹配http://ww2.sinaimg.cn/large/a15b4afegw1f52rdah5gfj21hk1564hc
    # ================使用Pattern匹配文本，获得全部匹配结果================
    find = pattern.findall(read_text)  # 列表形式存储的结果
    for i in range(len(find)):
        full_html = '<img src="' + find[i] + '" />'
        if full_html in check_set:
            pass
        else:
            check_set.add(full_html)
            info_line.append(full_html)

elif "http://imgsrc.baidu.com/forum/pic/item/" in read_text:
    # ================正则匹配================
    pattern = re.compile(r'http://imgsrc.baidu.com/forum/pic/item/[^)]*')
    # ================使用Pattern匹配文本，获得全部匹配结果================
    find = pattern.findall(read_text)  # 列表形式存储的结果
    for i in range(len(find)):
        info_line.append(find[i])

info = "\r\n".join(info_line)
print(info)
print(len(info_line))
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
