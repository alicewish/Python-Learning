import time, os

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
app_name = "PlistEdit Pro"
file_path_prefix = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/"
en_file_dir = file_path_prefix + app_name + "/en.lproj/"  # 输入文件的地址
cn_file_dir = file_path_prefix + app_name + "/zh_CN.lproj/"  # 输出文件的地址
untranslated_file_path = '/Users/alicewish/我的坚果云/' + app_name + '待翻译.txt'

# ================按行读取参考文本并字典化================
refer_file_path = "/Users/alicewish/Documents/GitHub/Mac-App-Translation/总词典.txt"  # 词典文件的地址
refer_dict = {}  # 创建一个字典
with open(refer_file_path) as fin:
    for line in fin:
        if "|" in line:  # 接受key|value格式
            refer_line = line.replace('\n', '')
            split_line = refer_line.split("|")
            key = split_line[0]
            value = split_line[1]
            refer_dict[key] = value

# ================英转中================
en_file_list = os.listdir(en_file_dir)  # 获得目录中的内容
for file_name in en_file_list:
    en_file_path = en_file_dir + file_name
    extension = os.path.splitext(en_file_path)[1]
    if extension == ".strings":
        en_readline = []
        cn_readline = []
        with open(en_file_path) as fin:
            for line in fin:
                en_line = (line.replace('\n', '')).replace('\t', '')
                en_readline.append(en_line)
                if "=" in en_line and "*" not in en_line:  # 接受key=value格式
                    split_line = en_line.split("=")
                    key = split_line[0].strip('"; ')
                    value = split_line[1].strip('"; ')
                    if value in refer_dict:
                        value = refer_dict[value]
                    else:
                        # ================写入文本================
                        f = open(untranslated_file_path, 'a')
                        try:
                            f.write(value + "\r\n")
                        finally:
                            f.close()
                    cn_line = '"' + key + '" = "' + value + '";'
                    cn_readline.append(cn_line)
    cn_file_path = cn_file_dir + file_name
    # ================写入文本================
    text = '\r\n'.join(cn_readline)
    print(text)

    f = open(cn_file_path, 'w')
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
