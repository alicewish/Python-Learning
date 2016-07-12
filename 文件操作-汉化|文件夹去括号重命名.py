import time, os, datetime, re

start_time = time.time()  # 初始时间戳
print(start_time)

file_dir = '/Volumes/Mack/汉化/'

file_list = os.listdir(file_dir) # 获得目录中的内容
print(file_list)

for file_name in file_list:
    file_path = file_dir + file_name
    # ================文件信息================

    is_dir = os.path.isdir(file_path)  # 判断目标是否目录

    last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(file_path))  # 最近访问时间
    created_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))  # 输出文件创建时间
    last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))  # 最近修改时间
    file_size = os.path.getsize(file_path)  # 输出文件大小（字节为单位）
    extension = os.path.splitext(file_path)[1]  # 拓展名
    line_info = [file_name, str(created_time), str(last_modified_time), str(last_access_time), str(file_size)]
    line = "\t".join(line_info)
    print(line)
    print(extension)

    if "(" in file_name and is_dir:
        matchs = re.match(r'\b[^()]*', file_name)
        new_file_name = matchs.group(0)
        if new_file_name[-1] == " ":
            new_file_name = new_file_name[:-1]
        new_file_path = file_dir + new_file_name + extension
        print(new_file_name)
        # ================按规则重命名================
        os.rename(file_path, new_file_path)  # 文件或目录都是使用这条命令

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
