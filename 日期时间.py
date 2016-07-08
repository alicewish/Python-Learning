import time;  # 引入time模块

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 格式化成June 10 2015形式
print(time.strftime("%B %d %Y", time.localtime()))

# 将格式字符串转换为时间戳
time_string = "June 10 2015"
time_convert = time.strptime(time_string, "%B %d %Y")
time_format = time.strftime("%Y-%m-%d", time_convert)
print(time_format)
