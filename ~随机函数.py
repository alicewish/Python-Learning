import time, random

start_time = time.time()  # 初始时间戳

# ================随机整数================
random_interger = random.randint(10, 20)
print(random_interger)

# ================随机单选================

sequence = ["a", "b", "c"]
random_choice = random.choice(sequence)
print(random_choice)

# ================随机多选================

sample = ['a', 'b', 'c', 'd']
random_sample = random.sample(sample, 3)
print(random_sample)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
