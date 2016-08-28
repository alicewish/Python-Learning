import time

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_name = "Localizable.strings"
app_name = "Keyboard Maestro"
file_path_prefix = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/"
input_file_path = file_path_prefix + app_name + "/" + file_name + ".txt"  # 输入文件的地址
primary_key_file_path = file_path_prefix + app_name + "/zh_CN.lproj/词典.txt"  # 词典文件的地址
refer_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/总词典.txt"  # 词典文件的地址
untranslated_file_path = file_path_prefix + app_name + "/zh_CN.lproj/未翻译.txt"  # 未翻译词典文件的地址
untranslated_English_file_path = file_path_prefix + app_name + "/zh_CN.lproj/未翻译英文.txt"  # 未翻译英文词典文件的地址

output_file_path = file_path_prefix + app_name + "/zh_CN.lproj/" + file_name + ".txt"  # 输出文件的地址
translated_file_path = file_path_prefix + app_name + "/zh_CN.lproj/已翻译.txt"  # 已翻译词典文件的地址

# ================按行读取参考文本并字典化================
primary_key_dict = {}  # 创建一个字典
with open(primary_key_file_path) as fin:
    for line in fin:
        refer_line = (line.replace('\n', '')).replace('\t', '')
        if "=" in refer_line:  # 接受key=value格式
            split_line = refer_line.split("=")
            primary_key_dict[split_line[0]] = split_line[1]

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
translated_readline = []  # 初始化按行存储数据列表,不接受换行符

check_set = set()  # 初始化为空集合
English_check_set = set()  # 初始化为空集合

with open(input_file_path) as fin:
    for line in fin:
        input_line = (line.replace('\n', '')).replace('\t', '')  # 无视换行和制表符
        output_line = input_line
        # 判断格式是否符合 key= "value";
        if "=" in input_line:
            split_line = input_line.split("=")
            primary_key = split_line[0].strip('" ')
            English = split_line[1].strip('"; ')
            if primary_key in primary_key_dict:
                Chinese = primary_key_dict[primary_key]
                print(Chinese)
                output_line = primary_key + '="' + Chinese + '";'
                translated_line = English + '|' + Chinese
                translated_readline.append(translated_line)
            elif English in refer_dict:
                Chinese = refer_dict[English]
                print(Chinese)
                output_line = primary_key + '="' + Chinese + '";'
                translated_line = English + '|' + Chinese
                translated_readline.append(translated_line)
            elif primary_key in check_set or English in English_check_set:
                pass
            else:  # 如果字典里没有则输出到未翻译表
                check_set.add(primary_key)
                English_check_set.add(English)
                f = open(untranslated_file_path, 'a')
                append_line = "\r\n" + input_line
                try:
                    f.write(append_line)
                finally:
                    f.close()

                if len(English) < 80:
                    f = open(untranslated_English_file_path, 'a')
                    append_line = "\r\n" + English
                    try:
                        f.write(append_line)
                    finally:
                        f.close()
        output_readline.append(output_line)

# ================写入文本================
text = '\r\n'.join(translated_readline)
print(text)

f = open(translated_file_path, 'w')
try:
    f.write(text)
finally:
    f.close()

# ================写入文本================
text = '\r\n'.join(output_readline)
print(text)

f = open(output_file_path, 'w')
try:
    f.write(text)
finally:
    f.close()

# ================写入剪贴板================
import pyperclip
pyperclip.copy(text)
spam = pyperclip.paste()

print(file_path_prefix + app_name + "/zh_CN.lproj")
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
