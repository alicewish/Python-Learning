from lxml import html
import requests

user_ID = '2217036742'
post_ID = "DADN2CjPN"
page = requests.get('http://m.weibo.com/' + user_ID + '/' + post_ID)
tree = html.fromstring(page.text)
content = tree.xpath('//meta[@name="description"]/@content')

print(page.text)
