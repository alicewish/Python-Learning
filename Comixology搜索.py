from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================
search_comic_name = 'Injustice: Gods Among Us: Year Five'  # 查询用漫画名

url_prefix = 'https://www.comixology.com/search?search='
comic_url = url_prefix + search_comic_name  # 完整的查询网址
# ========================执行区开始========================
page = requests.get(comic_url)  # 获取网页信息
tree = html.fromstring(page.text)  # 构筑查询用树
# ====================找到系列====================
all_url = tree.xpath('//a[@class="content-details"]/@href')
issues_url = []
check_set=set()
for i in range(len(all_url)):
    print(i)
    print(all_url[i])
    if re.match(r'.*/digital-comic/[^?]*', all_url[i]) and "Injustice" in all_url[i]:
        matchs = re.match(r'.*/digital-comic/[^?]*', all_url[i])
        short_link = matchs.group(0)
        if short_link not in check_set:
            issues_url.append(short_link)
        else:
            check_set.add(short_link)
# ========================输出区开始========================
print(len(issues_url))
text = '\r\n'.join(issues_url)
print(text)

# ================写入剪贴板================
import pyperclip

pyperclip.copy(text)
spam = pyperclip.paste()

# ================写入文本================
output_file_path = "/Users/alicewish/我的坚果云/分析用网页.htm"
f = open(output_file_path, 'w')
try:
    f.write(page.text)
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
