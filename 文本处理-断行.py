import time, jieba, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
dict_file_path = '/Users/alicewish/我的坚果云/userdict.txt'  # 自定义词典路径

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()
text_readline = read_text.splitlines()
# print(text_readline)

# ================按行读取文本:with open(更好)================
status_readline = []  # 状态列表
cut_readline = []  # 分词列表
output_readline = []  # 输出列表

jieba.load_userdict(dict_file_path)

for i in range(len(text_readline)):
    line = text_readline[i]
    length = len(line)
    if line == "":
        status = 0
    elif len(line) == 2 and re.match(r'[0-9][0-9]', line):
        status = -1
    else:
        status = 1
    status_readline.append(status)
    if status == 1:
        # ================结巴分词================
        string_list=[]
        seg_list = jieba.cut(text_readline[i])  # 默认是精确模式
        for word in seg_list:
            string_list.append(word)
        print(string_list)
        cut_line = "/".join(seg_list)
        cut_line = cut_line.replace("/的/", "的/")
        cut_line = cut_line.replace("/地/", "地/")
        cut_line = cut_line.replace("/得/", "得/")
        cut_line = cut_line.replace("/了/", "了/")
        cut_line = cut_line.replace("…/…", "……")
        cut_line = cut_line.replace("-/-", "--")
        print(cut_line)
        print(len(line))
        cut_readline.append(cut_line)
        # ================映射状态================

text = '\r\n'.join(cut_readline)

# ================写入剪贴板================
import pyperclip

pyperclip.copy(text)
spam = pyperclip.paste()
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
