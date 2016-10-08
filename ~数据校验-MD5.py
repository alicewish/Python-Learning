import time, requests

start_time = time.time()  # 初始时间戳
import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
print(hashlib.md5("whatever your string is".encode('utf-8')).hexdigest())

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

full_path='/Users/alicewish/Dropbox/Transformers - Primacy 001-002.psd'
print(hashlib.md5(open(full_path, 'rb').read()).hexdigest())

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
