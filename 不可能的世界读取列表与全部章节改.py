import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳

# ========================输入区开始========================
bookID = '10077'  # 图书ID
file_name = '他不喜欢超级英雄-竞天泽'  # 文件名

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名
url_prefix = 'http://www.8kana.com'  # 网址前缀
url_book = "/book/"  # 图书前缀
url_suffix = '.html'  # 网址后缀
url_read = "/read/"  # 章节前缀
book_url = url_prefix + url_book + bookID + url_suffix  # 完整图书网址

# ================按行读取参考文本================
refer_readline = []  # 初始化按行存储数据列表,不接受换行符
with open(txt_file_path) as fin:
    for line in fin:
        refer_readline.append(line)
progress = int(refer_readline[0])
print(progress)
# ========================执行区开始========================
page = requests.get(book_url)
tree = html.fromstring(page.text)
# ====================获取图书标题====================
book_title = tree.xpath('//title')[0]  # 图书标题
# ====================获取旧章节列表====================
chapter_old_name_list = tree.xpath('//a[@class="left"][@target="_blank"]/@title')  # 以列表形式存储的旧章节名称列表(过长会缩略)
# "他不喜欢超级英雄 001 序 他讨厌超级英..."
chapter_old_url_list = tree.xpath('//a[@class="left"][@target="_blank"]/@href')  # 以列表形式存储的旧章节地址列表
# "/read/10469.html"
# ====================获取最新6章列表====================
chapter_new_name_list = tree.xpath(
    '//a[@class="left chapter_con_a"][@target="_blank"]/@title')  # 以列表形式存储的新章节名称列表(过长会缩略)
# "他不喜欢超级英雄 001 序 他讨厌超级英..."
chapter_new_url_list = tree.xpath('//a[@class="left chapter_con_a"][@target="_blank"]/@href')  # 以列表形式存储的新章节地址列表
# "/read/10469.html"
# 第一个元素与第二个相同
# ====================合并到总章节列表====================
chapter_name_list = chapter_old_name_list + chapter_new_name_list  # 总章节名称列表
chapter_url_list = chapter_old_url_list + chapter_new_url_list  # 总章节地址列表
first_url = chapter_url_list.pop(0)  # 剥离章节地址列表第一个元素,因为重复
chapter_name_list_length = len(chapter_name_list)  # 计算章节名称数

chapterID_list = []  # 初始化章节ID列表
chapter_full_url_list = []  # 初始化章节完整网址列表
title_list = []  # 初始化章节标题列表
text_list = []  # 初始化章节内容列表

for i in range(chapter_name_list_length):
    chapterID_list.append(chapter_url_list[i][6:len(chapter_url_list[i]) - 5])  # 抽取章节ID
    chapter_full_url_list.append(url_prefix + url_read + chapterID_list[i] + url_suffix)  # 抽取完整图书章节网址

for i in range(progress, chapter_name_list_length):
    chapter_start_time = time.time()  # 章节开始读取时间戳
    refer_readline[0] = str(chapter_name_list_length)
    # ========================执行区开始========================
    page = requests.get(chapter_full_url_list[i])
    tree = html.fromstring(page.text)
    # ====================获取标题====================
    title = tree.xpath('//h2[@class="readbook_title"]/text()')[0]
    title_list.append(title)  # 标题
    print(title)
    # ====================获取段落====================
    paragraph_list = tree.xpath('//p[@id>0]/text()')  # 以列表形式存储的段落
    paragraphs = ''.join(paragraph_list)
    text_list.append(paragraphs)  # 将段落连接成字符串
    print(paragraphs)
    # ====================构筑文本====================
    refer_readline.append(title)
    refer_readline.append(paragraphs)
    # ==================操作TXT==================
    f = open(txt_file_path, 'w')
    text = "\r\n".join(refer_readline)  # 写入文本
    try:
        f.write(text)
    finally:
        f.close()
    # ================每章节时间计时================
    chapter_run_time = time.time() - chapter_start_time
    chapter_print = "第" + str(i + 1) + "页读取完毕," + "耗时:{:.4f}秒".format(chapter_run_time)
    print(chapter_print)

print(book_title)
print(book_url)
print(chapter_name_list_length)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
