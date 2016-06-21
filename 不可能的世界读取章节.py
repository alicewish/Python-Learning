import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================

chapterID = '106760'  # 章节ID

url_prefix = 'http://www.8kana.com'  # 网址前缀
url_book = "/read/"  # 章节前缀
url_suffix = '.html'  # 网址后缀
chapter_url = url_prefix + url_book + chapterID + url_suffix  # 完整图书章节网址
# ========================执行区开始========================
page = requests.get(chapter_url)
tree = html.fromstring(page.text)
# ====================获取标题====================
title = tree.xpath('//h2[@class="readbook_title"]/text()')[0]  # 标题
# ====================获取段落====================
paragraph_list = tree.xpath('//p[@id>0]/text()')  # 以列表形式存储的段落

text = ''.join(paragraph_list)  # 将段落连接成字符串

print(title)
print(text)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
