from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_name = '正则表达式字符串读取'  # 文件名

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名

# ========================执行区开始========================
# ==================操作TXT==================
f = open(txt_file_path, 'r')
read_text = f.read()  # 读取文本内容
# read_text="thumb150"
# print(read_text)

# 将正则表达式编译成Pattern对象
# 使用r前缀就不用考虑转义了
pattern = re.compile(r'http://ww2.sinaimg.cn/large/[^)]*')
# http://ww2.sinaimg.cn/large/a15b4afegw1f52rdah5gfj21hk1564hc
# 使用Pattern匹配文本，获得全部匹配结果
find = pattern.findall(read_text)#列表形式存储的结果

print(find)
print(len(find))

# if match:
#     # 使用Match获得分组信息
#     print(match.group())


# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
