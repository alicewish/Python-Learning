import time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================

file_name = '不义联盟第五年021填'  # 文件名

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名
# ================按行读取文本:with open(更好)================
text_readline = []  # 初始化按行存储数据列表,不接受结尾换行符
with open(txt_file_path) as fin:
    for line in fin:
        text_readline.append((line).replace('\n', ''))

# ================处理文本================
empty_line_number = -1
info=[]
# line_type = [0]
for i in range(len(text_readline)):
    if text_readline[i] == "":
        # line_type.append(0)
        last_empty_line_number = empty_line_number
        empty_line_number = i
        line_number = empty_line_number - last_empty_line_number - 1 #行数
        head=[str(i),"行数",str(line_number)]
        character_number = []
        character_count=0
        for j in range(line_number):
            character_number.append(str(len(text_readline[i-line_number+j])))
            character_count+=len(text_readline[i-line_number+j])
        end=head+[str(character_count)]+character_number
        see_this_line="\t".join(end)

        info_end=[str(line_number)]+[str(character_count)]+character_number
        info_line="\t".join(info_end)
        info.append(info_line)
        print(see_this_line)
    # elif re.match(r'[0-9][0-9]', text_readline[i]) and len(text_readline[i]) == 2:
    #     print(i, "页码:", text_readline[i])
    #     line_type.append(1)
    else:
        print(i,len(text_readline[i]), text_readline[i])
        # line_type.append(2)

all_info="\r\n".join(info)
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
