from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳

# 导入 gutenberg 集
from nltk.corpus import gutenberg

# 都有些什么语料在这个集合里？
print(gutenberg.fileids())
# ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']

# 导入 FreqDist 类
from nltk import FreqDist

# 频率分布实例化
fd = FreqDist()
# 统计文本中的词例
for word in gutenberg.words('austen-persuasion.txt'):
    fd.inc(word)

print(fd.N())  # total number of samples
# 98171
print(fd.B())  # number of bins or unique samples
# 6132
# 得到前 10 个按频率排序后的词
for word in fd.keys()[:10]:
    print(word, fd[word])

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
