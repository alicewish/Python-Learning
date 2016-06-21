import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
main_url = "http://icv2.com/articles/news/view/1850/"  # 完整文章网址
# ========================执行区开始========================
page = requests.get(main_url)
tree = html.fromstring(page.text)
# ====================获取本页名称====================
article_title = tree.xpath("//title/text()")[0]  # 文章名称

# ====================获取新文章列表====================
new_article_title_list = tree.xpath("//div[@class='article-text clearfix mrl5']/p/a/text()")  # 以列表形式存储的新文章名称列表
new_article_url_list = tree.xpath("//div[@class='article-text clearfix mrl5']/p/a/@href")  # 以列表形式存储的新文章地址列表
# ====================获取旧文章列表====================
old_article_title_list = tree.xpath("//div[@class='article-text clearfix mrl5']/a/text()")  # 以列表形式存储的旧文章名称列表
old_article_url_list = tree.xpath("//div[@class='article-text clearfix mrl5']/a/@href")  # 以列表形式存储的旧文章地址列表
# ====================合并文章列表====================
article_title_list = new_article_title_list + old_article_title_list  # 以列表形式存储的总文章名称列表
article_url_list = new_article_url_list + old_article_url_list  # 以列表形式存储的总文章地址列表
article_title_list_length = len(article_title_list)  # 总文章数



for i  in range(10):
    article_url = "http://icv2.com/articles/markets/view/33887/top-300-comics-actual-february-2016"  # 完整图书章节网址
    # ========================执行区开始========================
    page = requests.get(article_url)
    tree = html.fromstring(page.text)
    # ====================获取本页名称====================
    article_title = tree.xpath("//title/text()")[0]  # 文章名称
    # ====================获取排名====================
    rank = tree.xpath("//tr/td[1]/p/text()")  # 列表形式存储的排名RANK
    # ====================获取指数====================
    index = tree.xpath("//tr/td[2]/p/text()")  # 列表形式存储的指数INDEX
    # ====================获取刊名====================
    title = tree.xpath("//tr/td[3]/p/text()")  # 列表形式存储的刊名TITLE
    # ====================获取价格====================
    price = tree.xpath("//tr/td[4]/p/text()")  # 列表形式存储的价格PRICE
    # ====================获取出版商====================
    publisher = tree.xpath("//tr/td[5]/p/text()")  # 列表形式存储的出版商PUBLISHER
    # ====================获取估算销量====================
    quantity = tree.xpath("//tr/td[6]/p/text()")  # 列表形式存储的估算销量QUANTITY

# info = '\r\n'.join(rank)

print(article_title)
print(rank[0])
print(index[0])
print(title[0])
print(price[0])
print(publisher[0])
print(quantity[0])


# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
