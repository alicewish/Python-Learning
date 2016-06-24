from lxml import html
import requests, time
from urllib.parse import quote



start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================

search_comic_name = '"Injustice: Gods Among Us: Year Five (2015-) #20"'  # 查询用漫画名

url_prefix = 'http://www.bing.com/search?q='
search_part = search_comic_name + " comixology"
comic_url = (url_prefix + quote(search_part)).replace("%20", "+")  # 完整的查询网址
print(comic_url)



global header_info
header_info = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1581.2 Safari/537.36',
    'Host':'www.zhihu.com',
    'Origin':'http://www.zhihu.com',
    'Connection':'keep-alive',
    'Referer':'http://www.zhihu.com/people/zihaolucky/followers',
    'Content-Type':'application/x-www-form-urlencoded',
    }
#todo
# ========================执行区开始========================
page = requests.get(comic_url)  # 获取网页信息
tree = html.fromstring(page.text)  # 构筑查询用树
# ====================分期====================
issues_url = tree.xpath('//a[@target="_blank"]/@href')
for i in range(len(issues_url)):
    print(i)
    print(issues_url[i])
# ========================输出区开始========================

# print(issues_url[85])

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
