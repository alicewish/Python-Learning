import time, re

start_time = time.time()  # 初始时间戳

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()
text_readline = read_text.splitlines()

# ================按行读取输入文本================
output_readline = []  # 初始化按行存储数据列表,不接受换行符

for i in range(len(text_readline)):
    line = text_readline[i]
    input_line = (line.replace('\n', '')).replace('\t', '')  # 无视换行和制表符
    # 定位到<string>,判断是否英文
    if "<string>" in input_line and "<key>" not in input_line and "{" not in input_line and "=" not in input_line:
        string_content = (input_line.replace("<string>", "")).replace("</string>", "")
        print(string_content)
        if string_content[0:2] != "NS":
            output_readline.append(string_content)

text = '\r\n'.join(output_readline)
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
