import time, os, datetime, re, json, shutil

start_time = time.time()  # 初始时间戳

txt_file_path = "/Users/alicewish/我的坚果云/重命名文件地址.txt"
# ==============按行读取文本==============
text_readline = []  # 初始化按行存储数据列表
with open(txt_file_path) as fin:
    for line in fin:
        this_line = line.replace('\n', '')
        text_readline.append(this_line)

file_dir = '/Volumes/Mack/汉化/——/'

issue_number = 30
prefix = "Injustice- Gods Among Us - Year Five (2015-) 0"

zip_name = "Injustice - Gods Among Us- Year Five 0" + str(issue_number).zfill(2) + " (2016) (digital) (Alicewish).zip"
zip_path=file_dir+zip_name
if not os.path.exists(zip_path):  # 判断目标是否存在
    for i in range(len(text_readline)):
        file_path = text_readline[i]
        # ================文件信息================
        is_dir = os.path.isdir(file_path)  # 判断目标是否目录
        extension = os.path.splitext(file_path)[1]  # 拓展名
        extension_list = [".jpg"]
        if not is_dir and extension in extension_list:
            file_dir = os.path.split(file_path)[0]
            new_file_name = prefix + str(issue_number).zfill(2) + "-0" + str(i).zfill(2) + ".jpg"
            new_file_path = file_dir + "/" + new_file_name
            print(new_file_name)
            # ================按规则重命名================
            os.rename(file_path, new_file_path)  # 文件或目录都是使用这条命令
else:
    file_list = os.listdir(file_dir)  # 获得目录中的内容
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

        if extension == ".jpg":
            new_file_name = file_name.replace("Injustice- Gods Among Us - Year Five (2015-) ","第五年")

            new_file_path = file_dir + new_file_name
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
