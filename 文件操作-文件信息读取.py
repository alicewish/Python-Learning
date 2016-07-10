import time, os, datetime

start_time = time.time()  # 初始时间戳
print(start_time)

file = '/Users/alicewish/Dropbox/不义联盟第五年022.mp3'

last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(file))  # 最近访问时间
created_time = datetime.datetime.fromtimestamp(os.path.getctime(file))  # 输出文件创建时间
last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file))  # 最近修改时间


print(os.path.getatime(file))  # 输出最近访问时间
print(os.path.getctime(file))  # 输出文件创建时间
print(os.path.getmtime(file))  # 输出最近修改时间
print(os.path.getsize(file))  # 输出文件大小（字节为单位）
print(os.path.abspath(file))  # 输出绝对路径'/Volumes/Leopard/Users/Caroline/Desktop/1.mp4'
print(os.path.normpath(file))  # 输出'/Volumes/Leopard/Users/Caroline/Desktop/1.mp4'

localtime = time.asctime(time.localtime(os.path.getctime(file)))
print("asctime时间为 :", localtime)

localtime = time.gmtime(os.path.getctime(file))
print("gmtime时间为 :", localtime)


# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
