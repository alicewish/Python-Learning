import time, os, datetime, re
from os.path import join, getsize


# ================获取文件夹大小================
def GetFolderSize(path):
    TotalSize = 0
    for item in os.walk(path):
        for file in item[2]:
            try:
                TotalSize = TotalSize + getsize(join(item[0], file))
            except:
                print("文件遇到错误:  " + join(item[0], file))
    return TotalSize


start_time = time.time()  # 初始时间戳
print(start_time)

file_dir = '/Volumes/Mack/汉化/'

file_list = os.listdir(file_dir)  # 获得目录中的内容
print(file_list)

all_info = []
for file_name in file_list:
    file_path = file_dir + file_name
    # ================文件信息================
    is_dir = os.path.isdir(file_path)  # 判断目标是否目录
    if is_dir:
        has_PSD = 0
        is_published = ""
        entry_start_time = time.time()
        inside_file_list = os.listdir(file_path)  # 获得目录中的内容
        for inside_file_name in inside_file_list:
            inside_file_path = file_path + "/" + inside_file_name

            if inside_file_name == "成品": \
                    is_published = "1"
            # ================文件信息================
            last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(inside_file_path))  # 最近访问时间
            created_time = datetime.datetime.fromtimestamp(os.path.getctime(inside_file_path))  # 输出文件创建时间
            last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(inside_file_path))  # 最近修改时间
            file_size = os.path.getsize(inside_file_path)  # 输出文件大小（字节为单位）
            extension = os.path.splitext(inside_file_path)[1]  # 拓展名
            is_dir = os.path.isdir(inside_file_path)  # 判断目标是否目录
            inside_line_info = [inside_file_name, str(created_time), str(last_modified_time), str(last_access_time),
                                str(file_size)]
            line = "\t".join(inside_line_info)
            # print(line)
            # print(extension)
            if extension == ".psd":
                has_PSD += 1
        folder_size = float(GetFolderSize(file_path))  # 输出文件夹大小（字节为单位）
        last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(file_path))  # 最近访问时间
        created_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))  # 输出文件创建时间
        last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))  # 最近修改时间
        extension = os.path.splitext(file_path)[1]  # 拓展名
        line_info = [file_name, str(has_PSD), str(folder_size), is_published, str(created_time),
                     str(last_modified_time), str(last_access_time)]
        line = "\t".join(line_info)
        all_info.append(line)
        entry_run_time = time.time() - entry_start_time
        print(file_path, "耗时:{:.2f}秒".format(entry_run_time))

text = "\r\n".join(all_info)
# ================写入剪贴板================
import pyperclip

pyperclip.copy(text)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
