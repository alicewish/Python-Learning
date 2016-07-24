import time

start_time = time.time()  # 初始时间戳

# ================按行读取参考文本并字典化================
refer_dict = {}  # 创建一个字典
refer_file_path = "/Users/alicewish/我的坚果云/项目分类词典.txt"
with open(refer_file_path) as fin:
    for line in fin:
        refer_line = (line.replace('\n', ''))
        if "\t" in refer_line:  # 接受key value格式
            split_line = refer_line.split("\t")
            refer_dict[split_line[0]] = split_line[1]


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
    line_text=""
    for key in refer_dict:
        if key in text_readline[i]:
            line_text=refer_dict[key]
            print(line_text)
            # ================每项时间计时================
            entry_run_time = time.time() - entry_start_time
            entry_print = "耗时:{:.4f}秒".format(entry_run_time)
            print(i)
            print(entry_print)
    line_list.append(line_text)

info = "\r\n".join(line_list)
# print(info)
# # ================写入剪贴板================
# import pyperclip
#
# pyperclip.copy(info)
# spam = pyperclip.paste()
# ================写入TXT================
file_name = 'Timing Export-辅助.txt'
txt_file_path = '/Users/alicewish/我的坚果云/' + file_name  # TXT文件名
f = open(txt_file_path, 'w')
try:
    f.write(info)
finally:
    f.close()
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
