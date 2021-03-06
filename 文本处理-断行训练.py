import time, re

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
        print(entry_info_line)

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
        print(i, len(text_readline[i]), text_readline[i])

all_info = "\r\n".join(info_list)
# ================由频次排序================
for scenario in scenario_list:
    scenario_line_list = scenario.split("\t")
    scenario_count = str(1000-scenario_count_dict[scenario]).zfill(3)
    scenario_line_list.insert(1, scenario_count)
    scenario_line_full = '-'.join(scenario_line_list)
    scenario_list_full.append(scenario_line_full)

scenario_list_full.sort()
# scenario_list_full.reverse()

print(scenario_list_full)
# print(scenario_count_dict)

# ================pyperclip模块================
import pyperclip

pyperclip.copy(all_info)
spam = pyperclip.paste()
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
