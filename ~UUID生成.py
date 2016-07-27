import time, uuid

start_time = time.time()  # 初始时间戳
import uuid

name = "test_name"
namespace = "test_namespace"

print(uuid.uuid1())  # 带参的方法参见Python Doc
# print(uuid.uuid3(namespace, name))
# print(uuid.uuid4())
# print(uuid.uuid5(namespace, name))

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
