import time, os, shutil

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
Date = '2016.08.24'
refer_file_name = '0 Day Week移动.txt'
censor_dict_file_name = '度盘审查关键词.txt'

file_dir = '/Volumes/Mack/~Week 0-Day/0-Day Week of ' + Date
new_file_dir = os.path.join('/Volumes/Mack/——', Date + ' 0-Day')
dropbox_path = '/Users/alicewish/Dropbox'
refer_file_path = os.path.join(dropbox_path, refer_file_name)  # 词典文件的地址
censor_dict_file_path = os.path.join(dropbox_path, censor_dict_file_name)  # 审查词典的地址

method = -1  # 正向1,逆向-1

# ================按行读取审查关键词并字典化================
censor_dict = {}  # 创建一个字典
with open(censor_dict_file_path) as fin:
    for line in fin:
        refer_line = (line.replace('\n', '')).replace('\t', '')
        if "|" in refer_line:  # 接受key|value格式
            if method == 1:
                split_line = refer_line.split("|")
                censor_dict[split_line[0]] = split_line[1]
            elif method == -1:
                split_line = refer_line.split("|")
                censor_dict[split_line[1]] = split_line[0]

# ================按行读取参考文本并字典化================
refer_dict = {}  # 创建一个字典
with open(refer_file_path) as fin:
    for line in fin:
        refer_line = (line.replace('\n', '')).replace('\t', '')
        if "|" in refer_line:  # 接受key|value格式
            split_line = refer_line.split("|")
            refer_dict[split_line[0]] = split_line[1]
# output_readline = []

# ================读取文件夹内容================
file_list = os.listdir(file_dir)  # 获得目录中的内容
# print(file_list)
# file_list.sort()

# ================计数器初始化================
file_count = len(file_list)
print(file_count)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
m_max = file_count // 20 + 1
n_max = file_count % 20
print(m_max, n_max)

# ================建立分目录================
try:
    os.mkdir(new_file_dir)  # 创建目录
except:
    pass

for m in range(m_max):
    m_dir_name = Date + ' 0-Day-' + alphabet[m]
    file = os.path.join(new_file_dir, m_dir_name)
    try:
        os.mkdir(file)  # 创建目录
    except:
        pass
    if m < m_max - 1:
        for n in range(20):
            n_dir_name = str(n + 1).zfill(2)
            file = os.path.join(new_file_dir, m_dir_name, n_dir_name)
            try:
                os.mkdir(file)  # 创建目录
            except:
                pass
    elif m == m_max - 1:
        for n in range(n_max):
            n_dir_name = str(n + 1).zfill(2)
            file = os.path.join(new_file_dir, m_dir_name, n_dir_name)
            try:
                os.mkdir(file)  # 创建目录
            except:
                pass

# ================移动文件并记录================
i = 0
for file_name in file_list:
    new_file_name = file_name
    for word in censor_dict:
        new_word = censor_dict[word]
        if word in file_name:
            new_file_name = file_name.replace(word, new_word)
    m_i = i // 20
    n_i = i % 20
    m_dir_name = Date + ' 0-Day-' + alphabet[m_i]
    n_dir_name = str(n_i + 1).zfill(2)
    # is_dir = os.path.isdir(file_path)  # 判断目标是否目录
    # extension = os.path.splitext(file_path)[1]  # 拓展名

    file_path = os.path.join(file_dir, file_name)
    new_file_path = os.path.join(new_file_dir, m_dir_name, n_dir_name, new_file_name)
    shutil.move(file_path, new_file_path)  # 移动文件或目录都是使用这条命令
    path_print = os.path.join(Date + ' 0-Day', m_dir_name, n_dir_name, new_file_name)
    if file_name in refer_dict:
        if refer_dict[file_name] == path_print:  # 已存在
            pass
        else:
            print(file_name, refer_dict[file_name], path_print)  # 新地址
    else:
        output_line = "\r\n" + file_name + '|' + path_print
        # output_readline.append(output_line)
        f = open(refer_file_path, 'a')
        try:
            f.write(output_line)
        finally:
            f.close()
    # print(file_name)
    i = i + 1

# ================写入文本================
# text = '\r\n'.join(output_readline)
# print(text)

# f = open(refer_file_path, 'a')
# try:
#     f.write(text)
# finally:
#     f.close()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
