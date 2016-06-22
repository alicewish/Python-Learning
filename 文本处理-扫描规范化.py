from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
input_file_name = '正则表达式匹配测试'  # 输入文件的名称
output_file_name = '正则表达式匹配测试处理'  # 输出文件的名称

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
input_file_path = path_prefix + input_file_name + '.txt'  # 输入文件的地址
output_file_path = path_prefix + output_file_name + '.txt'  # 输出文件的地址

# ================按行读取文本:with open(更好)================
text_readline = []  # 初始化按行存储数据列表
with open(input_file_path) as fin:
    for line in fin:
        text_readline.append(line)

# ================处理文本================

new_text_readline = []  # 初始化按行存储数据列表

# ================结尾不为句点则将下一行拼入本行================

for i in range(len(text_readline) - 1):
    if re.match(r"\?", text_readline[i][-1]):  # 结尾为句点
        new_text_readline.append(text_readline[i])
    else:  # 结尾不为句点
        new_text_readline.append(text_readline[i] + text_readline[i + 1])

# ================打印文本================
for i in range(len(text_readline)):
    print(new_text_readline[i], end="")
print(len(new_text_readline))

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
