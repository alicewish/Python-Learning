from lxml import html
import requests

ID = "1788862154"
ID = "1461874162"

page = requests.get('http://sinacn.weibodangan.com//user/' + ID)
tree = html.fromstring(page.text)
nickname = tree.xpath('//h3[@class="username"]/text()')[0]

print('微博名', nickname)
