from lxml import html
import requests, urllib.parse, time

start_time = time.time()
search_term = 'Hitlist Week'
file_path = '/Users/alicewish/我的坚果云/Hitlist Week地址.txt'
f = open(file_path, 'w')
thispage = requests.get('https://kat.cr/usearch/' + search_term + '/1/?field=time_add&sorder=desc')
tree = html.fromstring(thispage.text)
dataparams = tree.xpath('//a[@class="turnoverButton siteButton bigButton"]/text()')
page_number = int(dataparams[-1])
text = search_term + " Full List\r\n"
try:
    f.write(text)
finally:
    f.close()
for i in range(1, page_number):
    thispage = requests.get('https://kat.cr/usearch/' + search_term + '/' + str(i) + '/?field=time_add&sorder=desc')
    tree = html.fromstring(thispage.text)
    dataparams = tree.xpath('//div[@class="none"]/@data-sc-params')
    for j in range(0, 24):
        data = eval(dataparams[j])  # 将字符串转化成字典dict类型

        name = urllib.parse.unquote(data['name'])
        extension = urllib.parse.unquote(data['extension'])
        magnet = urllib.parse.unquote(data['magnet'])

        info = (name, magnet, '')
        text = '\r\n'.join(info)

        f = open(file_path, 'a')
        try:
            f.write(text)
        finally:
            f.close()
# 计时模块
run_time = time.time() - start_time
if run_time < 60:
    print("耗时: {:.2f}秒".format(run_time))
elif run_time < 3600:
    print("耗时: {:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:
    print("耗时: {:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
