from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
input_file_path = "/Users/alicewish/Downloads/my.md"
# ================按行读取输入文本================
read_text = open(input_file_path, 'r').read()  # 读取文本

text_readline = read_text.replace("\nclass", "class").splitlines()
# print(text_readline)

# readline = []  # 初始化按行存储数据列表,不接受换行符

for i in range(len(text_readline)):
    text_readline[i] = re.sub(r'<span.*</span>', '', text_readline[i])  # 去除span
    text_readline[i] = text_readline[i].replace('……', '…')

    markdown_line = text_readline[i].replace("\*", "の")
    print(markdown_line)
    line_cut_list = markdown_line.split("*")
    print(line_cut_list)

    plain_line = markdown_line.replace("\*", "の").replace("*", "").replace("の", "*")  # 调整*
    print(plain_line)

    line_formmat_list = []

    for j in range(len(plain_line)):
        line_formmat_list.append(0)
    # print(line_formmat_list)

    line_mark_count_list = []
    for k in range(len(plain_line) + 1):
        line_mark_count_list.append(0)

    point = 0
    for char in markdown_line:
        if char == '*':
            line_mark_count_list[point] = line_mark_count_list[point] + 1
        else:
            point = point + 1
    print(line_mark_count_list)

    pin = 0
    before = 0

    for seg in line_cut_list:
        if seg == '':
            pass
        else:
            last_pin = pin
            pin += len(seg)
            # print(line_mark_count_list[last_pin])
            # print(line_mark_count_list[pin])
            if last_pin > 0:
                before = line_formmat_list[last_pin - 1]

            for l in range(last_pin, pin):
                if before != 3:
                    line_formmat_list[l] = before + line_mark_count_list[last_pin]
                if before == 3:
                    line_formmat_list[l] = before - line_mark_count_list[last_pin]
            # print(line_formmat_list[last_pin - 1])
    print(line_formmat_list)




# readline.append(text_readline[i])

# text = "\r\n".join(readline)
# print(text)
# # ================写入剪贴板================
# import pyperclip
#
# pyperclip.copy(text)
# spam = pyperclip.paste()
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
