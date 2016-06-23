import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================

article_url = "http://icv2.com/articles/comics/view/14743/top-300-comics-actual-march-2009"  # 完整图书章节网址
# ========================执行区开始========================
page = requests.get(article_url)
tree = html.fromstring(page.text)
# ====================获取本页名称====================
article_title = tree.xpath("//title/text()")[0]  # 文章名称
# ====================获取排名====================
rank = tree.xpath("//tr/td[1]/p/span/text()")  # 列表形式存储的排名RANK
# ====================获取指数====================
index = tree.xpath("//tr/td[2]/p/span/text()")  # 列表形式存储的指数INDEX
# ====================获取刊名====================
title = tree.xpath("//tr/td[3]/p/span/text()")  # 列表形式存储的刊名TITLE
# ====================获取价格====================
price = tree.xpath("//tr/td[4]/p/span/text()")  # 列表形式存储的价格PRICE
# ====================获取出版商====================
publisher = tree.xpath("//tr/td[5]/p/span/text()")  # 列表形式存储的出版商PUBLISHER
# ====================获取估算销量====================
quantity = tree.xpath("//tr/td[6]/p/span/text()")  # 列表形式存储的估算销量QUANTITY
quantity_format = []
for i in range(len(quantity)):
    number = (quantity[i].replace(",", "")).strip()
    quantity_format.append(number)

info_list=[]
for i in range(len(rank)):
    line=rank[i]+"\t"+index[i]+"\t"+title[i]+"\t"+price[i]+"\t"+publisher[i]+"\t"+quantity_format[i]+"\t"+article_title
    info_list.append(line)

info = '\r\n'.join(info_list)

print(article_title)
print(rank[0])
print(index[0])
print(title[0])
print(price[0])
print(publisher[0])
print(quantity[0])
print(info)



# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
