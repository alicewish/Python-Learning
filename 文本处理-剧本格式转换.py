from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_dir = "/Users/alicewish/我的坚果云/"
input_file_name = "剧本格式待转换.txt"
output_file_name = "剧本格式已转换.txt"
input_file_path = file_dir + input_file_name
output_file_path = file_dir + output_file_name
character_list = ['字幕', '屏幕显示', '蝙蝠侠', '蝙蝠侠（独白）', '女性记者', '少女（画格外）', '阿莱克西斯·卢瑟', '阿莱克西斯·卢瑟（画格外）', '莱克斯·卢瑟', '蝙蝠侠（画格外）']
# ================按行读取输入文本================
input_readline = []  # 初始化按行存储数据列表,不接受换行符
with open(input_file_path) as fin:
    for line in fin:
        readline = line.replace('\n', '')
        input_readline.append(readline)

output_readline = [input_readline[0]]
for i in range(2, len(input_readline)):
    line = input_readline[i]
    if "画页" in line and len(line) < 5:  # 画页
        output_line = "<h1>" + line + "</h1>"
    elif "画格" in line and len(line) < 5:  # 画格
        output_line = "<h2>" + line + "</h2>"
    elif line in character_list:  # 人物
        output_line = "<h3><center><u>" + line + "</u></center></h3>"
    elif "（" in line and input_readline[i - 1] in character_list:  # 括号
        output_line = '<p style="margin: 0.0px 48.0px">' + line + "</p>"
    elif "画格" in input_readline[i - 1] and len(input_readline[i - 1]) < 5:  # 画格说明
        output_line = line
    else:  # 对话
        output_line = '<p style="margin: 0.0px 24.0px">' + line + "</p>"

    output_readline.append(output_line)

# ================写入文本================
text = '\r\n'.join(output_readline)
print(text)

f = open(output_file_path, 'w')
try:
    f.write(text)
finally:
    f.close()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
