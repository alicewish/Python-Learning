from lxml import html
import requests, urllib.parse, time

start_time = time.time()
user = 'Nemesis43'
file_path = '/Users/alicewish/我的坚果云/Nemesis43地址.txt'
f = open(file_path, 'w')
thispage = requests.get('https://kat.cr/user/' + user + '/uploads/?page=1')
tree = html.fromstring(thispage.text)
dataparams = tree.xpath('//a[@class="turnoverButton siteButton bigButton"]/text()')
page_number = int(dataparams[-1])
try:
    f.write(user)
finally:
    f.close()
for i in range(1, page_number):
    thispage = requests.get('https://kat.cr/user/' + user + '/uploads/?page=' + str(i))
    tree = html.fromstring(thispage.text)
    dataparams = tree.xpath('//div[@class="none"]/@data-sc-params')
    for j in range(0, 24):
        data = eval(dataparams[j])  # 将字符串转化成字典dict类型

        name = urllib.parse.unquote(data['name'])
        extension = urllib.parse.unquote(data['extension'])
        magnet = urllib.parse.unquote(data['magnet'])

        info = '\n' + name + '\n' + magnet + '\n'
        # print(info)

        f = open(file_path, 'a')
        try:
            f.write(info)
        finally:
            f.close()
print("耗时: {:.2f}s".format(time.time() - start_time))
