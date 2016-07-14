import time, os

start_time = time.time()  # 初始时间戳

name = "PyCharm"
en_file_dir = '/Users/alicewish/Documents/GitHub/Mac-App-Translation/' + name + '/resources_en/messages/'
cn_file_dir = '/Users/alicewish/Documents/GitHub/Mac-App-Translation/' + name + '/resources_cn/messages/'
untranslated_file_path = '/Users/alicewish/我的坚果云/' + name + '待翻译.txt'

# ================按行读取参考文本并字典化================
refer_dict = {}  # 创建一个字典
refer_file_dir = '/Users/alicewish/Documents/GitHub/Mac-App-Translation/' + name + '/PyCharm-zh_CN-4.5.3/zh_CN/'
refer_file_list = os.listdir(refer_file_dir)  # 获得目录中的内容
for file_name in refer_file_list:
    refer_file_path = refer_file_dir + file_name
    with open(refer_file_path) as fin:
        for line in fin:
            refer_line = (line.replace('\n', '')).replace('\t', '')
            if "=" in refer_line:  # 接受key=value格式
                split_line = refer_line.split("=")
                refer_dict[split_line[0]] = split_line[1]

refer_file_dir = '/Users/alicewish/Documents/GitHub/Mac-App-Translation/' + name + '/WebStorm9汉化版/zh_CN/'
refer_file_list = os.listdir(refer_file_dir)  # 获得目录中的内容
for file_name in refer_file_list:
    refer_file_path = refer_file_dir + file_name
    with open(refer_file_path) as fin:
        for line in fin:
            refer_line = (line.replace('\n', '')).replace('\t', '')
            if "=" in refer_line:  # 接受key=value格式
                split_line = refer_line.split("=")
                refer_dict[split_line[0]] = split_line[1]

# ================英转中================
en_file_list = os.listdir(en_file_dir)  # 获得目录中的内容
for file_name in en_file_list:
    en_file_path = en_file_dir + file_name
    en_readline = []
    cn_readline = []
    with open(en_file_path) as fin:
        for line in fin:
            en_line = (line.replace('\n', '')).replace('\t', '')
            en_readline.append(en_line)
            if "=" in en_line:  # 接受key=value格式
                split_line = en_line.split("=")
                key = split_line[0]
                value = split_line[1]
                if key in refer_dict:
                    value = refer_dict[key]
                else:
                    # ================写入文本================
                    f = open(untranslated_file_path, 'a')
                    try:
                        f.write(en_line + "\r\n")
                    finally:
                        f.close()
                cn_line = key + "=" + value
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
