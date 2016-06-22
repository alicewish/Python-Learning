from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳

user_ID = '2217036742'
post_ID = "DADN2CjPN"
page = requests.get('http://m.weibo.com/' + user_ID + '/' + post_ID)
tree = html.fromstring(page.text)
content = tree.xpath('//meta[@name="description"]/@content')

print(page.text)
