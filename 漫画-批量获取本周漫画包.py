import time,requests,urllib
from lxml import html

start_time = time.time()  # 初始时间戳
# ==================参数区开始==================
search_order = '/?field=time_add&sorder=desc'  # 搜索的顺序
search_domain = 'https://kat.cr/usearch/'  # 搜索的网站地址
# ==================执行区开始==================
search_term = ['DC Week','Marvel Week','Hitlist Week','Novus Week','0-Day Week']  # 搜索的关键词

magnet_list = []
for i in range(len(search_term)):
    # ================读取第1页================
    this_page = requests.get(search_domain + search_term[i] + '/' + str(1) + search_order)
    tree = html.fromstring(this_page.text)
    dataparams = tree.xpath('//div[@class="none"]/@data-sc-params')
    # data-sc-params形如{ 'name': '...', 'extension': 'cbr', 'magnet': '...' },dataparams是列表
    # ==============读取第1项==============
    data = eval(dataparams[0])  # 将字符串转化成字典dict类型,设为data
    name = urllib.parse.unquote(data['name'])  # 获取文件名
    print(name)
    magnet = urllib.parse.unquote(data['magnet'])  # 获取磁力链接
    magnet_list.append(magnet)

text = '\r\n'.join(magnet_list)  # 将文本设为信息断行拼合
print(text)
# ================写入剪贴板================
import pyperclip
pyperclip.copy(text)
spam = pyperclip.paste()
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
