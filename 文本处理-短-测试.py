from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
input_file_name = '测试文本'  # 输入文件的名称
output_file_name = '测试文本处理'  # 输出文件的名称

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
input_file_path = path_prefix + input_file_name + '.txt'  # 输入文件的地址
output_file_path = path_prefix + output_file_name + '.txt'  # 输出文件的地址


# ========================函数区开始========================
# ====================去标点格式化====================
def normalize(s):
    """Convert s to a normalized string.  """
    # 包含所有要保留的字符的集合
    keep = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', '-', "'"]
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result


# ====================制作词频词典====================
def make_freq_dict(text):
    """
    Returns a dictionary whose keys are the words of (text), and whose values are the counts of those words.
    """
    words = text.split()
    dict = {}
    for w in words:
        if w in dict:  # 看到w出现过？
            dict[w] += 1
        else:
            dict[w] = 1
    return dict


# ====================计算并显示给定文本文件的统计数据====================
def print_file_stats(s):
    """Print statistics for the given file.
    """
    num_chars = len(s)  # 在规范化s 之前计算字符数
    num_lines = s.count('\n')  # 在规范化s 之前计算行数
    d = make_freq_dict(s)
    num_words = sum(d[w] for w in d)  # 计算s 包含多少个单词
    #  创建一个列表，其中的元素由出现次数和单词组成的元组
    lst = [(d[w], w) for w in d]
    #  并按出现次数从高到低排列
    lst.sort()  # 正序
    lst.reverse()  # 翻转
    #  在屏幕上打印结果
    print("文件有: ")
    print(" %s 个字母" % num_chars)
    print(" %s 行" % num_lines)
    print(" %s 个单词" % num_words)
    # ==============频数最高的10个单词==============
    print("\n频数最高的10个单词是:")
    i = 1  # i 为列表元素编号
    for count, word in lst[:10]:
        print('%2s. %4s %s' % (i, count, word))
        i += 1


# ========================输出区开始========================
text = open(input_file_path, 'r').read()  # 读取文本
lower_text = text.lower()  # 将文本全部变为小写
normalized_text = normalize(text)  # 对文本格式化
dict = make_freq_dict(normalized_text)  # 制作词频词典

print('长度:', len(text))
print('行数:', text.count('\n'))
print('词数(未处理):', len(text.split()))
print('词(未处理)\n:', text.split())
print('词数(处理后):', len(normalize(text).split()))
print('词(处理后):\n', normalize(text).split())
print('词频词典:\n', dict)
print('文本文件的统计数据:\n', print_file_stats(text))

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
