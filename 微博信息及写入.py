import requests, time
from lxml import html

start_time = time.time()

ID = "1788862154"

page = requests.get('http://sinacn.weibodangan.com//user/' + ID)
tree = html.fromstring(page.text)
name = tree.xpath('//h3[@class="username"]/text()')
data = tree.xpath('//td/text()')
info = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '昵称 ' + name[0], '好友 ' + data[
    0], '粉丝 ' + data[1].strip(), '微博 ' + data[2], '', '')
text = '\r\n'.join(info)
print(text)
f = open('/Users/alicewish/我的坚果云/微博.txt', 'a')
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
