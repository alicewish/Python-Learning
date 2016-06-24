from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================

search_comic_name = 'Injustice: Gods Among Us: Year Five (2015-) #20'  # 查询用漫画名
url_prefix = 'https://www.comixology.com/search?search='
comic_url = url_prefix + search_comic_name  # 完整的查询网址
# ========================执行区开始========================
page = requests.get(comic_url)  # 获取网页信息
tree = html.fromstring(page.text)  # 构筑查询用树
# ====================分期====================
issues_url = tree.xpath('//a[@class="content-details"]/@href')
for i in range(len(issues_url)):
    print(i)
    print(issues_url[i])
# ========================输出区开始========================

print(issues_url[85])

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
