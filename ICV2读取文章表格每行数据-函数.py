import requests, time, os
from lxml import html

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

    print(article_title)
    print(info)

    text = '\r\n'.join(output_readline)

    # ================写入CSV================

    output_file_name = article_title.replace("ICv2: ", "") + '.csv'

    output_file_path = os.path.join(store_path, output_file_name)
    f = open(output_file_path, 'w')
    try:
        f.write(text)
    finally:
        f.close()

    # ================运行时间计时================
    run_time = time.time() - start_time
    if run_time < 60:  # 两位小数的秒
        show = "耗时:{:.2f}秒".format(run_time)
    elif run_time < 3600:  # 分秒取整
        show = "耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60)
    else:  # 时分秒取整
        show = "耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60)

    return show

article_url = "http://icv2.com/articles/markets/view/35546/top-300-comics-actual-august-2016"  # 网址
print(read_article(article_url))