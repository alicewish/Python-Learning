import time, os, datetime

start_time = time.time()  # 初始时间戳
print(start_time)

file = '/Users/alicewish/Dropbox/不义联盟第五年022.mp3'

last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(file))  # 最近访问时间
created_time = datetime.datetime.fromtimestamp(os.path.getctime(file))  # 输出文件创建时间
last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file))  # 最近修改时间

print(last_access_time)
print(created_time)
print(last_modified_time)

print(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(file))))  # 格式化时间

print(datetime.date.today())
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
