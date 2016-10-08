import time, os

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
refer_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/总词典.txt"  # 词典文件的地址

# ================按行读取参考文本并字典化================
refer_dict = {}  # 创建一个字典
with open(refer_file_path) as fin:
    for line in fin:
        refer_line = (line.replace('\n', '')).replace('\t', '')
        if "|" in refer_line:  # 接受key|value格式
            split_line = refer_line.split("|")
            refer_dict[split_line[0]] = split_line[1]

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
translated_readline = []  # 初始化按行存储数据列表,不接受换行符

count = 0

for i in range(len(text_readline)):
    line = text_readline[i]
    input_line = (line.replace('\n', '')).replace('\t', '')  # 无视换行和制表符
    output_line = input_line
    if "=" in input_line and "*" not in input_line:  # 接受key=value格式
        split_line = input_line.split("=")
        primary_key = split_line[0].strip('; ').strip('"')
        value = split_line[1].strip('; ').strip('"')
        split_line = text_readline[i-1].split('"')
        English=split_line[3]
        if English in refer_dict:
            Chinese = refer_dict[English]
            output_line = '"' + primary_key + '" = "' + Chinese + '";'
            translated_check_set.add(Chinese)
            count = count + 1
            English_and_Chinese = str(i + 1) + "\t" + English + "\t" + Chinese
            translated_readline.append(English_and_Chinese)
        elif English in untranslated_check_set:
            output_line = '"' + primary_key + '" = "' + English + '";'  #
        else:  # 如果字典里没有则附在字典结尾
            untranslated_check_set.add(English)
            f = open(refer_file_path, 'a')
            append_line = "\r\n" + English
            try:
                f.write(append_line)
            finally:
                f.close()
            output_line = '"' + primary_key + '" = "' + English + '";'  #

    output_readline.append(output_line)

# ================写入文本================
text = '\r\n'.join(output_readline)
translated_text = '\r\n'.join(translated_readline)

print(text)
print("已翻译:", count)
print(translated_text)
print("未翻译:", len(untranslated_check_set))
print(untranslated_check_set)

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
