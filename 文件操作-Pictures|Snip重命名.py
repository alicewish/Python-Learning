import time, os

start_time = time.time()  # 初始时间戳
print(start_time)

file_dir = '/Users/alicewish/Pictures/'

file_list = os.listdir(file_dir)  # 获得目录中的内容
print(file_list)

all_info = []
ordinal_num = 0
alphabet="ABCDEFGHI"
for file_name in file_list:
    file_path = file_dir + file_name
    # ================文件信息================
    is_dir = os.path.isdir(file_path)  # 判断目标是否目录
    extension = os.path.splitext(file_path)[1]  # 拓展名
    extension_list = [".jpg"]
    if not is_dir and extension in extension_list and "拷贝" in file_name and "Snip" in file_name:
        print(ordinal_num)
        print(file_name)
        # ================按规则重命名================
        prefix = "【生肉】【不义联盟-第五年】【30】【承诺】"
        new_file_name = prefix+alphabet[ordinal_num]
        new_file_path = file_dir + new_file_name
        print(new_file_name)
        # ================按规则重命名================
        os.rename(file_path, new_file_path)  # 文件或目录都是使用这条命令
        ordinal_num += 1

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
