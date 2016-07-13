import time, os, datetime, re, json

start_time = time.time()  # 初始时间戳
print(start_time)

file_dir = '/Users/alicewish/Desktop/临时上传/'

file_list = os.listdir(file_dir)  # 获得目录中的内容
print(file_list)

all_info = []
for file_name in file_list:
    file_path = file_dir + file_name
    # ================文件信息================
    is_dir = os.path.isdir(file_path)  # 判断目标是否目录
    extension = os.path.splitext(file_path)[1]  # 拓展名
    extension_list = [".jpg"]
    if not is_dir and extension in extension_list and "地球2会社" in file_name:
        new_file_name = file_name.replace("地球2会社", "2号地球：会社")
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
