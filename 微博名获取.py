from lxml import html
import requests

ID = "1788862154"
page = requests.get('http://sinacn.weibodangan.com//user/' + ID)
tree = html.fromstring(page.text)
nickname = tree.xpath('//h3[@class="username"]/text()')

print('微博名', nickname[0])
