import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
output_file_name = 'ICV2销量数据'  # 输出文件的名称

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
output_file_path = path_prefix + output_file_name + '.txt'  # 输出文件的地址
main_url = "http://icv2.com/articles/news/view/1850/"  # 完整文章网址
# ========================执行区开始========================
page = requests.get(main_url)
tree = html.fromstring(page.text)
# ====================获取本页名称====================
main_title = tree.xpath("//title/text()")[0]  # 文章名称

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
# ====================新样式数据读取====================
for j in range(70):
    entry_start_time = time.time()
    try:
        # ====================读取文章表格每行数据-新====================
        article_url = article_url_list[j]  # 完整图书章节网址
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
        quantity_format = []
        for k in range(len(quantity)):
            number = (quantity[k].replace(",", "")).strip()
            quantity_format.append(number)
        info_list = []
        for i in range(len(rank)):
            line = rank[i] + "\t" + index[i] + "\t" + title[i] + "\t" + price[i] + "\t" + publisher[i] + "\t" + \
                   quantity_format[i] + "\t" + article_title
            info_list.append(line)
        info = '\r\n'.join(info_list)
        info += '\r\n'
        print(info)
        f = open(output_file_path, 'a')
        try:
            f.write(info)
        finally:
            f.close()
    except:
        print("从第", j, "项开始数据变化")
    # ================每项时间计时================
    entry_run_time = time.time() - entry_start_time
    entry_print = "第" + str(j + 1) + "页耗时:{:.4f}秒".format(entry_run_time)
    print(entry_print)

# ====================旧样式数据读取====================
for j in range(70, len(article_title_list)):
    entry_start_time = time.time()
    try:
        # ====================读取文章表格每行数据-新====================
        article_url = article_url_list[j]  # 完整图书章节网址
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
        for k in range(len(quantity)):
            number = (quantity[k].replace(",", "")).strip()
            quantity_format.append(number)
        info_list = []
        for i in range(len(rank)):
            line = rank[i] + "\t" + index[i] + "\t" + title[i] + "\t" + price[i] + "\t" + publisher[i] + "\t" + \
                   quantity_format[i] + "\t" + article_title
            info_list.append(line)
        info = '\r\n'.join(info_list)
        info += '\r\n'
        print(info)
        f = open(output_file_path, 'a')
        try:
            f.write(info)
        finally:
            f.close()
    except:
        print("从第", j, "项开始数据变化")
    # ================每项时间计时================
    entry_run_time = time.time() - entry_start_time
    entry_print = "第" + str(j + 1) + "页耗时:{:.4f}秒".format(entry_run_time)
    print(entry_print)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
