import time, jieba, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
txt_file_path = '/Users/alicewish/我的坚果云/不义联盟第五年填字合并.txt'  # TXT文件名
# ================按行读取文本:with open(更好)================
text_readline = []  # 初始化按行存储数据列表,不接受结尾换行符
status_readline = []

with open(txt_file_path) as fin:
    for line in fin:
        line = line.replace('\n', '')
        line = line.replace('……', '…')
        if line == '':
            status = '空行'
        elif len(line) == 10 and re.match(r'不义联盟第五年[0-9]{3}', line):
            status = '标题'
        elif len(line) == 2 and re.match(r'[0-9]{2}', line):
            status = '页码'
        elif len(line) > 20 and ('*' in line or '[' in line):
            status = '注释'
        else:
            status = '文本'
        text_readline.append(line)
        status_readline.append(status)

# ================删除不必要信息================
process_readline = text_readline

for i in range(len(process_readline)):
    if status_readline[i] == '标题':
        for j in range(7):
            process_readline[i + j] = ''
    elif status_readline[i] == '页码':
        for j in range(1):
            process_readline[i + j] = ''
    elif status_readline[i] == '注释':
        for j in range(1):
            process_readline[i + j] = ''

# ================处理文本================
empty_line_number = -1  # 初始化空行
info_list = []
scenario_count_dict = {}
scenario_list = []
scenario_list_full = []

for i in range(0, len(process_readline)):
    if process_readline[i] == "":
        last_empty_line_number = empty_line_number  # 上一空行
        empty_line_number = i  # 这一空行
        line_number = empty_line_number - last_empty_line_number - 1  # 断行行数
        character_number_list = []  # 每行字数初始化
        character_count = 0  # 总字数初始化
        for j in range(line_number):
            line = process_readline[i - line_number + j]
            character_number_list.append(str(len(line)))
            character_count += len(line)
        store_entry = "\t".join(character_number_list)
        entry_info = [str(i), "断行行数", str(line_number), "总字数", str(character_count).zfill(2), "分配", store_entry]
        entry_info_line = "\t".join(entry_info)
        # print(entry_info_line)

        info_detail = [str(line_number)] + [str(character_count).zfill(2)] + character_number_list
        info_line = "\t".join(info_detail)
        # ================建立查询列表================
        # 总字数-断行方案
        if character_count > 0 and character_count < 70:
            info_list.append(info_line)
            scenario = str(character_count).zfill(2) + '\t' + store_entry
            if scenario in scenario_list:
                scenario_count_dict[scenario] = scenario_count_dict[scenario] + 1
            else:
                scenario_list.append(scenario)
                scenario_count_dict[scenario] = 1

    else:
        pass
        # print(i, len(text_readline[i]), text_readline[i])

all_info = "\r\n".join(info_list)
# ================由频次排序================
for scenario in scenario_list:
    scenario_line_list = scenario.split("\t")
    scenario_count = str(1000 - scenario_count_dict[scenario]).zfill(3)
    scenario_line_list.insert(1, scenario_count)
    scenario_line_full = '-'.join(scenario_line_list)
    scenario_list_full.append(scenario_line_full)

scenario_list_full.sort()
# scenario_list_full.reverse()

print(scenario_list_full)
# print(scenario_count_dict)

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
    line = line.replace('……', '…')
    print(line)
    print(len(line))

    if line == "":
        status = 0  # 空行
    elif len(line) == 2 and re.match(r'[0-9][0-9]', line):
        status = -1  # 页码
    else:
        status = 1  # 待分词
    status_readline.append(status)
    if status == 1:
        # ================结巴分词================
        string_list = []
        seg_list = jieba.cut(line)  # 默认是精确模式
        for word in seg_list:
            string_list.append(word)
        print(string_list)

        start_status = False
        for i in range(len(scenario_list_full)):
            scenario_line_full = scenario_list_full[i]
            if scenario_line_full[0:2] == str(len(line)).zfill(2):
                if start_status:
                    end_i = i
                else:
                    start_i = i
                    start_status = True
                    end_i = i
        # ================进行切分================
        current_i = start_i

        cut_right = False
        while current_i <= end_i and not cut_right:
            current_cut = scenario_list_full[current_i]
            current_cut_list = current_cut[7:].split("-")  # 列表存储的切分方案
            # ================进行分词判断================
            line_can_cut_list = []

            for i in range(len(line)):
                line_can_cut_list.append(0)

            j = 0
            for string in string_list:
                j = j + len(string)
                # print(j)
                line_can_cut_list[j - 1] = 1

            for i in range(len(line)):
                if line[i] in ',.?!，。…？！”·-':
                    line_can_cut_list[i - 1] = 0
                elif line[i] in '“':
                    line_can_cut_list[i] = 0
                elif line[i] in '中的地得了吗吧' and line_can_cut_list[i - 1]==1 and line_can_cut_list[i]==1:
                    line_can_cut_list[i - 1] = 0

            print(line_can_cut_list)
            print(current_cut_list)

            # ================判断方案正确与否================

            sum = 0
            cut_right = True
            for i in range(len(current_cut_list)):
                last_sum=sum
                sum = sum + int(current_cut_list[i])
                print(line_can_cut_list[sum - 1])
                print(line[last_sum:sum])

                if line_can_cut_list[sum - 1] == 0:
                    cut_right = False
            print(cut_right)
            if not cut_right:
                current_i += 1
        if cut_right:
            sum = 0
            for i in range(len(current_cut_list)):
                last_sum=sum
                sum = sum + int(current_cut_list[i])
                output_readline.append(line[last_sum:sum])
        else:
            output_readline.append(line)
    else:
        output_readline.append(line)

# ================写入剪贴板================
text = '\r\n'.join(output_readline)

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
