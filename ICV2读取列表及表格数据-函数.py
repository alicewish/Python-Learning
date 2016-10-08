import requests, time, os
from lxml import html

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
main_url = "http://icv2.com/articles/news/view/1850/"  # 完整文章网址

now_date = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳

dropbox_path = '/Users/alicewish/Dropbox'

output_readline = []
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


# ========================函数区开始========================

# ================CSV格式规范================
def csvconvert(string):
    converted_string = string.replace('"', '""')
    return converted_string


# ================运行时间计时================
def runtime(start_time):
    run_time = time.time() - start_time
    if run_time < 60:  # 两位小数的秒
        show_time = "{:.2f}秒".format(run_time)
    elif run_time < 3600:  # 分秒取整
        show_time = "{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60)
    else:  # 时分秒取整
        show_time = "{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60)
    return show_time


# ================读取网页表格并保存================
def read_article(article_url):
    start_time = time.time()  # 初始时间戳
    # ========================输入区开始========================
    store_path = '/Users/alicewish/Dropbox/ICV2'
    output_readline = []
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
    for i in range(len(quantity)):
        number = (quantity[i].replace(",", "")).strip()
        quantity_format.append(number)

    info_list = []
    for i in range(len(rank)):
        output_line_in_list = [rank[i], index[i], title[i], price[i], publisher[i], quantity_format[i], article_title]
        output_line = ",".join(output_line_in_list)
        output_readline.append(output_line)
        line = "\t".join(output_line_in_list)
        info_list.append(line)

    info = '\r\n'.join(info_list)

    print(article_title, len(rank))
    print(info)

    text = '\r\n'.join(output_readline)

    if len(rank) > 10:
        # ================写入CSV================
        output_file_name = article_title.replace("ICv2: ", "") + '.csv'
        output_file_path = os.path.join(store_path, output_file_name)
        f = open(output_file_path, 'w')
        try:
            f.write(text)
        finally:
            f.close()
    else:
        print("未成功获取")
    return runtime(start_time)


def index():
    info = ""  # 初始化信息字符串为空
    for i in range(article_title_list_length):
        info += article_title_list[i] + "\n"
        info += article_url_list[i] + "\n"
        output_line_in_list = [csvconvert(article_title_list[i]), csvconvert(article_url_list[i])]
        output_line = '"' + '","'.join(output_line_in_list) + '"'
        output_readline.append(output_line)

    print(article_title)
    print(main_url)
    print(info)
    print(article_title_list_length)

    text = '\r\n'.join(output_readline)

    # ================写入CSV================

    output_file_name = article_title.replace("ICv2: ", "") + '.csv'

    output_file_path = os.path.join(dropbox_path, output_file_name)
    f = open(output_file_path, 'w')
    try:
        f.write(text)
    finally:
        f.close()


# index()


# ========================ICV2读取文章表格每行数据========================
for i in range(article_title_list_length):
    article_url = article_url_list[i]
    article_title = article_title_list[i]
    if 'Top' in article_title:
        try:
            print(read_article(article_url))
        except:
            print(article_url, "未读取")
    print("进度:{:.2f}%".format(i / article_title_list_length * 100), i)

print("总耗时:", runtime(start_time))
