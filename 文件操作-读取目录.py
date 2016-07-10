import time, os, datetime

start_time = time.time()  # 初始时间戳
print(start_time)

file_dir = '/Users/alicewish/Dropbox/'

file_list = os.listdir(file_dir)
print(file_list)

for file_name in file_list:
    file_path = '/Users/alicewish/Dropbox/' + file_name

    last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(file_path))  # 最近访问时间
    created_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))  # 输出文件创建时间
    last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))  # 最近修改时间
    file_size = os.path.getsize(file_path)  # 输出文件大小（字节为单位）
    line_info = [file_name,str(created_time), str(last_modified_time), str(last_access_time), str(file_size)]
    line = "\t".join(line_info)
    print(line)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
