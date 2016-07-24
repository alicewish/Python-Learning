import time, os, datetime, re, json

start_time = time.time()  # 初始时间戳
print(start_time)

file_dir = '/Users/alicewish/Google 云端硬盘/'

file_list = os.listdir(file_dir)  # 获得目录中的内容
print(file_list)

google_drive_dict = {}
for file_name in file_list:
    file_path = file_dir + file_name
    # ================文件信息================
    is_dir = os.path.isdir(file_path)  # 判断目标是否目录
    extension = os.path.splitext(file_path)[1]  # 拓展名
    extension_list = [".gdoc", ".gsheet", ".gscript"]
    if not is_dir and extension in extension_list:
        read_text = open(file_path, 'rb').read()  # 读取文本
        decoded_text = str(read_text)[2:-1]
        data = json.loads(decoded_text)  # 将json字符串转换成python对象
        url = data["url"]
        doc_id = data["doc_id"]
        email = data["email"]
        resource_id = data["resource_id"]
        google_drive_dict[doc_id] = file_name

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()
text_readline = read_text.splitlines()
print(text_readline)
print(len(text_readline))

line_list = []
for i in range(len(text_readline)):
    entry_start_time = time.time()
    line_text = text_readline[i]
    for key in google_drive_dict:
        if key in text_readline[i]:
            line_text = google_drive_dict[key]
            print(i)
            print(line_text)

            # ================每项时间计时================
            entry_run_time = time.time() - entry_start_time
            entry_print = "耗时:{:.4f}秒".format(entry_run_time)
            print(entry_print)
    line_list.append(line_text)
info = "\r\n".join(line_list)
# print(info)
# ================写入剪贴板================
import pyperclip

pyperclip.copy(info)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
