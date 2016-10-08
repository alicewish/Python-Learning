import time, os

start_time = time.time()  # 初始时间戳

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()
text_readline = read_text.splitlines()
print(text_readline)

# ================按行读取输入文本================
output_readline = []  # 初始化按行存储数据列表,不接受换行符
untranslated_check_set = set()  # 初始化为空集合
translated_check_set = set()  # 初始化为空集合

count = 0

for i in range(len(text_readline)):
    line = text_readline[i]
    input_line = (line.replace('\n', '')).replace('\t', '')  # 无视换行和制表符
    if "=" in input_line and "*" not in input_line:  # 接受key=value格式
        split_line = input_line.split("=")
        English = (split_line[0].strip('; '))[1:-1]
        value = (split_line[1].strip('; '))[1:-1]
        output_line = English + "\t" + value
        output_readline.append(output_line)

text = '\r\n'.join(output_readline)
print(text)

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
