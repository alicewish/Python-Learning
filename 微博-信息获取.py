import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳

# ========================输入区开始========================
ID = "1788862154"  # 微博用户ID

url_prefix = 'http://sinacn.weibodangan.com//user/'
full_url = url_prefix + ID

# ========================执行区开始========================
page = requests.get(full_url)
tree = html.fromstring(page.text)
nickname = tree.xpath('//h3[@class="username"]/text()')[0]
data = tree.xpath('//td/text()')
friends = data[0]
fans = data[1].replace(" ", "")
posts = data[2]
location = tree.xpath("//div[@class='info'][1]/text()")[0]
description = tree.xpath("//div[@class='info'][2]/text()")[0]
alldays = tree.xpath("//div[@class='hidden-xs hidden-sm']/p[1]/text()")[0]
days = alldays[7:]
started = tree.xpath("//span[@id='register_time']/text()")[0]
info = (nickname, friends, fans, posts, location, description, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), days)

text = '\t'.join(info)
print(text)
# ================写入剪贴板================
import pyperclip
pyperclip.copy(text)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
