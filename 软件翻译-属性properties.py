from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_name = "ActionsBundle.properties"
input_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/PyCharm/resources_en/messages/" + file_name  # 输入文件的地址
refer_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/PyCharm/PyCharm-zh_CN-4.5.3/zh_CN/" + file_name  # 词典文件的地址
output_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/PyCharm/resources_cn/messages/" + file_name  # 输出文件的地址

# ================按行读取输入文本================
input_readline = []  # 初始化按行存储数据列表,不接受换行符
with open(input_file_path) as fin:
    for line in fin:
        input_readline.append((line).replace('\n', ''))

# ================按行读取参考文本================
refer_readline = []  # 初始化按行存储数据列表,不接受换行符
with open(refer_file_path) as fin:
    for line in fin:
        refer_readline.append((line).replace('\n', ''))

# ========================输入字典化========================
input_dict = {}  # 创建一个字典
for i in range(len(input_readline)):
    if "=" in input_readline[i]:
        split_line = input_readline[i].split("=")
        key = split_line[0]
        value = split_line[1]
        input_dict[key] = value
# print(key, input_dict[key])
# print(len(input_dict))
# ========================参考字典化========================
refer_dict = {}  # 创建一个字典
for i in range(len(refer_readline)):
    if "=" in refer_readline[i]:
        split_line = refer_readline[i].split("=")
        key = split_line[0]
        value = split_line[1]
        refer_dict[key] = value
# print(key, refer_dict[key])
# print(len(refer_dict))
# ========================建立输出字典========================
output_dict = input_dict
for key in refer_dict:
    output_dict[key] = refer_dict[key]

output_readline = []
for key, value in output_dict.items():
    line = key + "=" + value
    output_readline.append(line)
    # print(line)
# ========================检查缺失键值========================
for key in input_dict:
    if not refer_dict.get(key):
        print(key, "\r\n", input_dict.get(key))
# # ================写入文本================
# text = '\r\n'.join(output_readline)
# print(text)
#
# f = open(output_file_path, 'w')
# try:
#     f.write(text)
# finally:
#     f.close()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
