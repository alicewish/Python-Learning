import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
bookID = '10077'  # 图书ID

url_prefix = 'http://www.8kana.com'  # 网址前缀
url_book = "/book/"  # 图书前缀
url_suffix = '.html'  # 网址后缀
book_url = url_prefix + url_book + bookID + url_suffix  # 完整图书网址
# ========================执行区开始========================
page = requests.get(book_url)
tree = html.fromstring(page.text)
# ====================获取旧章节列表====================
chapter_name_list = tree.xpath('//a[@class="left"][@target="_blank"]/@title')  # 以列表形式存储的旧章节名称列表
# "他不喜欢超级英雄 001 序 他讨厌超级英..."
chapter_url_list = tree.xpath('//a[@class="left"][@target="_blank"]/@href')  # 以列表形式存储的旧章节地址列表
# "/read/10469.html"
chapter_name_list_length = len(chapter_name_list)  # 计算章节名称数
chapter_url_list_length = len(chapter_name_list)  # 计算章节地址数
chapter_name_list_text = '\r\n'.join(chapter_name_list)  # 将章节名称列表连接成字符串
chapter_url_list_text = '\r\n'.join(chapter_url_list)  # 将章节地址列表连接成字符串
info = ""  # 初始化信息字符串为空
for i in range(chapter_name_list_length):
    info += chapter_name_list[i] + "\n"
    info += url_prefix + chapter_url_list[i + 1] + "\n"
# ====================获取新章节列表====================
chapter_new_name_list = tree.xpath('//a[@class="left chapter_con_a"][@target="_blank"]/@title')  # 以列表形式存储的新章节名称列表
# "他不喜欢超级英雄 001 序 他讨厌超级英..."
chapter_new_url_list = tree.xpath('//a[@class="left chapter_con_a"][@target="_blank"]/@href')  # 以列表形式存储的新章节地址列表
# "/read/10469.html"
chapter_new_name_list_length = len(chapter_new_name_list)  # 计算新章节名称数
chapter_new_url_list_length = len(chapter_new_name_list)  # 计算新章节地址数
chapter_new_name_list_text = '\r\n'.join(chapter_new_name_list)  # 将新章节名称列表连接成字符串
chapter_new_url_list_text = '\r\n'.join(chapter_new_url_list)  # 将新章节地址列表连接成字符串
for i in range(chapter_new_name_list_length):
    info += chapter_new_name_list[i] + "\n"
    info += url_prefix + chapter_new_url_list[i] + "\n"

print(chapter_name_list_length + chapter_new_name_list_length)
print(chapter_url_list_length + chapter_new_url_list_length)
print(book_url)
print(info)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
