from lxml import html
import requests, time
from string import maketrans  # 引用 maketrans 函数。

start_time = time.time()

# 语法:str.translate(table[, deletechars]);
# 其中table是一个翻译表，通过maketrans方法得来
# deletechars是你需要删除的内容

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)  # 定义该翻译表

str = "this is string example....wow!!!"
print(str.translate(trantab, 'tg')) # 将字符串以翻译表的规则进行替换输出并删除其中的字母t与g
# h3s 3s str3n 2x1mpl2....w4w!!!

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
