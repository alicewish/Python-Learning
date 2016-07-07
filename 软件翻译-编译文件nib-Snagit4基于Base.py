import time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_name = "CalloutToolProperties.nib"
app_name = "Snagit4"
language_name = "Base"

file_path_prefix = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/"
input_file_path = file_path_prefix + app_name + "/" + language_name + ".lproj/" + file_name + ".txt"  # 输入文件的地址
refer_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/总词典.txt"  # 词典文件的地址
output_file_path = file_path_prefix + app_name + "/zh_CN.lproj/" + file_name + ".txt"  # 输出文件的地址

# ================按行读取参考文本并字典化================
refer_dict = {}  # 创建一个字典
with open(refer_file_path) as fin:
    for line in fin:
        refer_line = (line.replace('\n', '')).replace('\t', '')
        if "|" in refer_line:  # 接受key|value格式
            split_line = refer_line.split("|")
            refer_dict[split_line[0]] = split_line[1]

# ================按行读取输入文本================
output_readline = []  # 初始化按行存储数据列表,不接受换行符
check_set = set()  # 初始化为空集合
with open(input_file_path) as fin:
    for line in fin:
        input_line = (line.replace('\n', '')).replace('\t', '')  # 无视换行和制表符
        output_line = input_line
        # 定位到<string>,判断是否英文
        if "<string>" in input_line and "<key>" not in input_line and ".title" not in input_line:
            English = (input_line.replace("<string>", "")).replace("</string>", "")
            status_English = False  # 初始化状态为非翻译文本
            if len(English) > 1 and re.match(r'\b[A-Z][a-z]{1,}[^.]', English) and len(English) < 80:  # 如果首字母大写，说明可翻译
                status_English = True
            if len(English) > 18 and " " not in English:  # 如果长词无空格，说明不可翻译
                status_English = False
            # 如果是英文则翻译
            if status_English:
                if English in refer_dict:
                    Chinese = refer_dict[English]
                    output_line = "<string>" + Chinese + "</string>"
                elif English in check_set:
                    pass
                else:  # 如果字典里没有则附在字典结尾
                    check_set.add(English)
                    f = open(refer_file_path, 'a')
                    append_line = "\r\n" + English
                    try:
                        f.write(append_line)
                    finally:
                        f.close()
        output_readline.append(output_line)

# ================写入文本================
text = '\r\n'.join(output_readline)
print(text)

f = open(output_file_path, 'w')
try:
    f.write(text)
finally:
    f.close()

print(file_path_prefix + app_name + "/zh_CN.lproj")
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
