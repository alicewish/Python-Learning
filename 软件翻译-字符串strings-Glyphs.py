from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_name = "Localizable.strings"
app_name = "Glyphs"
file_path_prefix = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/"
input_file_path = file_path_prefix + app_name + "/en.lproj/" + file_name + ".txt"  # 输入文件的地址
refer_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/总词典.txt"  # 词典文件的地址
output_file_path = file_path_prefix + app_name + "/zh_CN.lproj/" + file_name + ".txt"  # 输出文件的地址

# ================按行读取输入文本================
input_readline = []  # 初始化按行存储数据列表,不接受换行符
with open(input_file_path) as fin:
    for line in fin:
        input_line = (line.replace('\n', '')).replace('\t', '')
        input_readline.append(input_line)
# ========================输入字典化========================
input_dict = {}  # 创建一个字典
# 接受key= "value";格式
for i in range(len(input_readline)):
    if "=" in input_readline[i]:
        split_line = input_readline[i].split("=")
        raw_key = split_line[0]
        raw_value = split_line[1]
        split_key = raw_key.split('"')
        key = split_key[1]
        split_value = raw_value.split('"')
        value = split_value[1]
        input_dict[key] = value
        print(key, input_dict[key])
print(len(input_dict))
# ================按行读取参考文本================
refer_readline = []  # 初始化按行存储数据列表,不接受换行符
with open(refer_file_path) as fin:
    for line in fin:
        refer_line = line.replace('\n', '')
        refer_readline.append(refer_line)
# ========================参考字典化========================
refer_dict = {}  # 创建一个字典
# 接受key|value格式
for i in range(len(refer_readline)):
    if "|" in refer_readline[i]:
        split_line = refer_readline[i].split("|")
        key = split_line[0]
        value = split_line[1]
        refer_dict[key] = value
# ========================建立输出字典========================
output_dict = input_dict
for key in input_dict:
    if refer_dict.get(key):
        output_dict[key] = refer_dict[key]

output_readline = []
for key, value in output_dict.items():
    line = '"'+key + '" = "' + value + '";'
    output_readline.append(line)
    print(line)
# ========================检查缺失键值========================
check_set = set()
for key in input_dict:
    if not refer_dict.get(key):
        check_set.add(key)
        f = open(refer_file_path, 'a')
        append_line = "\r\n" + key
        try:
            f.write(append_line)
        finally:
            f.close()
        print(key, "\r\n", input_dict.get(key))
# ================写入文本================
text = '\r\n'.join(output_readline)
# print(text)

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
