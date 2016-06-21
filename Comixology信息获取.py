from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================

comic_name = 'Batman-2016-1'  # 查询用漫画名
comic_ID = "366119"  # 查询用漫画ID
url_prefix = 'https://www.comixology.com/'
url_middle = '/digital-comic/'
comic_url = url_prefix + comic_name + url_middle + comic_ID  # 完整的查询网址
# print(comic_url)
# ========================执行区开始========================
page = requests.get(comic_url)  # 获取网页信息
tree = html.fromstring(page.text)  # 构筑查询用树
# ====================标题====================
title = tree.xpath('//h2[@class="title"]/text()')[0]
# ====================简介====================
raw_description = tree.xpath('//section[@class="item-description"]/text()')
description = "".join(raw_description)
# ====================价格====================
price = tree.xpath('//h5[@class="item-price"]/text()')[0]
# ====================创作信息====================
raw_credits = tree.xpath('//div[@class="credits"]/*/text()')
credit = "\n".join(raw_credits)
credits = (credit.replace('\t', '')).replace("\n\n\n","")
print(len(raw_credits))

# ========================输出区开始========================
info_list = ("标题: " + title, "价格: " + price, "简介: " + description, "创作信息" + credits)
info = "\r\n".join(info_list)
print(info)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
