from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)
# 这将创建buyers的列表：
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# 这将创建prices的列表：
prices = tree.xpath('//span[@class="item-price"]/text()')

print('Buyers: ', buyers)
print('Prices: ', prices)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
