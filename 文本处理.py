from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
input_file_name = 'DC Comics - Bombshells 004'  # 输入文件的名称
output_file_name = 'DC Comics - Bombshells 004处理'  # 输出文件的名称

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
input_file_path = path_prefix + input_file_name + '.txt'  # 输入文件的地址
output_file_path = path_prefix + output_file_name + '.txt'  # 输出文件的地址


# ========================函数区开始========================
# 包含所有要保留的字符的集合


def normalize(s):
    """Convert s to a normalized string.  """
    keep = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', '-', "'"]
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
            return result

# d.keys()
# 是一个列表，包含文件中所有不同的单词。
# len(d.keys())
# 是文件中不同的单词数。
# sum(d[k] for k in d)
# 是d中所有值之和，即文件包含的单词总数（包括重复的单词）。sum是一个Python内置函数，返回序列的总和。字典存储的数据未经排序，因此要获取一个清单，按出现次数从高到低的顺序列出所有单词，需要将字典转换为元组列表，如下所示。
lst = []
for k in d:  pair = (d[k], k)
lst.append(pair)
#todo

# ========================输出区开始========================

text = open(input_file_path, 'r').read()  # 读取文本

print('长度:', len(text))
print('行数:', text.count('\n'))
print('词数(未处理):', len(text.split()))
print('词(未处理):', text.split())
print('词数(处理后):', len(normalize(text).split()))
print('词(处理后):', normalize(text).split())
# print('词(转小写):', text.lower())
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
