import time, os, shutil

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
# Date = '2015.10.28'
censor_dict_file_name = '度盘审查关键词.txt'

out_file_dir = '/Volumes/Mack/~Week 0-Day/'
# file_dir = '/Volumes/Mack/~Week 0-Day/0-Day Week of ' + Date
dropbox_path = '/Users/alicewish/Dropbox'

censor_dict_file_path = os.path.join(dropbox_path, censor_dict_file_name)  # 审查词典的地址

method = -1  # 正向1,逆向-1

change_count = 0
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

# ================读取外文件夹内容================
out_file_list = os.listdir(out_file_dir)  # 获得目录中的内容

for dir_name in out_file_list:
    file_dir=os.path.join(out_file_dir, dir_name)
    print(file_dir)
    # ================读取内文件夹内容================
    file_list = os.listdir(file_dir)  # 获得目录中的内容

    # ================计数器初始化================
    file_count = len(file_list)
    print("文件数", file_count)

    # ================移动文件并记录================

    for file_name in file_list:

        new_file_name = file_name
        for word in censor_dict:
            new_word = censor_dict[word]
            if word in file_name:
                new_file_name = file_name.replace(word, new_word)
                change_count += 1
        if new_file_name != file_name:
            print(file_name)
        file_path = os.path.join(file_dir, file_name)
        new_file_path = os.path.join(file_dir, new_file_name)
        shutil.move(file_path, new_file_path)  # 移动文件或目录都是使用这条命令

        # is_dir = os.path.isdir(file_path)  # 判断目标是否目录
        # extension = os.path.splitext(file_path)[1]  # 拓展名

    print("修改数", change_count)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
