from lxml import html
import requests

page = requests.get('https://kat.cr/usearch/0%20day%20week/?field=time_add&sorder=desc')
tree = html.fromstring(page.text)
source = tree.xpath("//a[@class='cellMainLink']/@href")

print('分页地址 ', source[0])
