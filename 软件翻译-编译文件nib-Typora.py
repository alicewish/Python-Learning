from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_name = "Document.nib"
app_name = "Typora"
file_path_prefix = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/"
input_file_path = file_path_prefix + app_name + "/Base.lproj/" + file_name + ".txt"  # 输入文件的地址
refer_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/总词典.txt"  # 词典文件的地址
output_file_path = file_path_prefix + app_name + "/zh_CN.lproj/" + file_name + ".txt"  # 输出文件的地址

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
# ================按行读取输入文本================
input_readline = []  # 初始化按行存储数据列表,不接受换行符
output_readline = []
check_set = set()
with open(input_file_path) as fin:
    for line in fin:
        input_line = (line.replace('\n', '')).replace('\t', '')
        output_line = input_line
        # 定位到<string>,判断是否英文
        if "<string>" in input_line and "<key>" not in input_line and ".title" not in input_line:
            English = (input_line.replace("<string>", "")).replace("</string>", "")
            status = False
            if len(English) > 2 and re.match(r'\b[A-Z][a-z]{2,}[^.]', English) and len(English) < 42:
                status = True
            if "⌘" in English:
                status = True
            if len(English) > 18 and " " not in English:
                status = False
            if status:
                if English in refer_dict:
                    Chinese = refer_dict[English]
                    output_line = "<string>" + Chinese + "</string>"
                elif English in check_set:
                    pass
                else:
                    check_set.add(English)
                    f = open(refer_file_path, 'a')
                    append_line = "\r\n" + English
                    try:
                        f.write(append_line)
                    finally:
                        f.close()
        output_readline.append(output_line)

# ========================建立输出字典========================

# ========================检查缺失键值========================

# ================写入文本================
text = '\r\n'.join(output_readline)
# print(text)

f = open(output_file_path, 'w')
try:
    f.write(text)
finally:
    f.close()

# print(file_path_prefix + app_name + "/zh_CN.lproj")
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
