import requests, time
from lxml import html

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳

# ========================输入区开始========================
ID = "1788862154"  # 微博用户ID
file_name = '微博' + now  # 文件名

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名
url_prefix = 'http://sinacn.weibodangan.com//user/'
full_url = url_prefix + ID

# ========================执行区开始========================
page = requests.get(full_url)
tree = html.fromstring(page.text)
name = tree.xpath('//h3[@class="username"]/text()')[0]
data = tree.xpath('//td/text()')
info = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '昵称 ' + name, '好友 ' + data[0], '粉丝 ' + data[1].strip(),
        '微博 ' + data[2], '\r\n')

text = '\r\n'.join(info)
print(text)

f = open(txt_file_path, 'a')
try:
    f.write(text)
finally:
    f.close()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
