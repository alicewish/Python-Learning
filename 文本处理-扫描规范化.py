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
text_readline = []  # 初始化按行存储数据列表,不接受结尾换行符
with open(input_file_path) as fin:
    for line in fin:
        text_readline.append((line).replace('\n', ''))
print(text_readline)
# ========================处理文本========================
# ====================去除空行====================
filled_text_readline = []  # 初始化按行存储数据列表
for i in range(len(text_readline)):
    if text_readline[i] == "":
        pass
        # print("空行")
    else:
        filled_text_readline.append(text_readline[i])

# ================结尾不为句点则在句末做标记================
new_text_readline = []  # 初始化按行存储数据列表
for i in range(len(filled_text_readline)):
    if filled_text_readline[i] == "":
        print("空行")
    elif re.match(r"[\.?!\"-]", (filled_text_readline[i])[-1]):  # 结尾为句点
        print((filled_text_readline[i])[-1] + "匹配:", filled_text_readline[i])
        new_text_readline.append(filled_text_readline[i])
    else:  # 结尾不为句点
        print((filled_text_readline[i])[-1] + "不匹配:" + filled_text_readline[i])
        print("转为:")
        print(filled_text_readline[i] + "接")
        new_text_readline.append(filled_text_readline[i] + "接")

# ================写入文本================
text = '\r\n'.join(new_text_readline)
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
