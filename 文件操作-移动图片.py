from lxml import html
import requests, time, os, shutil

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
refer_file_path="/Users/alicewish/我的坚果云/绝对地址.txt"
new_path="/Users/alicewish/Pictures/往期/"
old_path="/Users/alicewish/Pictures/屏幕快照 2016-05-26 上午1.42.57.png"
# ================按行读取参考文本================
with open(refer_file_path) as fin:
    for line in fin:
        old_path=line.replace('\n', '')
        try:
            shutil.copy(old_path, new_path)
        except:
            pass

shutil.copy(old_path, new_path)


# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
