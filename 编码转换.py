from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳
print('\u4e2d\u6587')
print('ABC'.encode('ascii'))
# b'ABC'
print('中文'.encode('utf-8'))
# b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii'))
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
print(b'ABC'.decode('ascii'))
# 'ABC'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# '中文'
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
