import time, jieba, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================

file_name = '不义联盟第五年023填字'  # 文件名
dict_name = 'userdict'  # 词典名
path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名
dict_file_path = path_prefix + dict_name + '.txt'  # TXT文件名

# ================按行读取文本:with open(更好)================
text_readline = []  # 初始化按行存储数据列表,不接受结尾换行符
with open(txt_file_path) as fin:
    for line in fin:
        text_readline.append((line).replace('\n', ''))

jieba.load_userdict(dict_file_path)

for i in range(len(text_readline)):
    print(text_readline[i])
    if text_readline[i] == "":
        print("空行")
    elif re.match(r'[0-9][0-9]', text_readline[i]):
        print("页码", text_readline[i])
    else:
        seg_list = jieba.cut(text_readline[i])  # 默认是精确模式
        print("/".join(seg_list))
        print(len(text_readline[i]))

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
