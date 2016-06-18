from lxml import html
import requests, time

start_time = time.time()
comic_name = 'Batman-2016-1'
comic_ID = "366119"
page = requests.get('https://www.comixology.com/' + comic_name + '/digital-comic/' + comic_ID)
tree = html.fromstring(page.text)
title = tree.xpath('//h2[@class="title"]/text()')[0]
raw_description = tree.xpath('//section[@class="item-description"]/text()')
description = "".join(raw_description)
price = tree.xpath('//h5[@class="item-price"]/text()')[0]

info_list = ("标题: " + title, "价格: " + price, "简介: " + description)
info = "\r\n".join(info_list)
print(info)
#计时模块
run_time = time.time() - start_time
if run_time < 60:
    print("耗时: {:.2f}秒".format(run_time))
elif run_time < 3600:
    print("耗时: {:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:
    print("耗时: {:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
