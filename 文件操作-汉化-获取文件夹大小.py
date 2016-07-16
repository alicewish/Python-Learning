import time
start_time = time.time()  # 初始时间戳

file_dir = '/Volumes/Mack/汉化/'

import os
from os.path import join, getsize, isfile, isdir, splitext
def GetFolderSize(path):
    TotalSize = 0
    for item in os.walk(path):
        for file in item[2]:
            try:
                TotalSize = TotalSize + getsize(join(item[0], file))
            except:
                print("文件遇到错误:  " + join(item[0], file))
    return TotalSize
print(float(GetFolderSize(file_dir))/1024/1024/1024)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
