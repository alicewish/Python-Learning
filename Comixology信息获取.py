from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================
comic_name = 'Batman-2016-1'  # 查询用漫画名
comic_ID = "366119"  # 查询用漫画ID

url_prefix = 'https://www.comixology.com/'
url_middle = '/digital-comic/'
comic_url = url_prefix + comic_name + url_middle + comic_ID  # 完整的查询网址
print(comic_url)

# ========================执行区开始========================
page = requests.get(comic_url)  # 获取网页信息
tree = html.fromstring(page.text)  # 构筑查询用树
# ====================标题====================
title = tree.xpath('//h2[@class="title"]/text()')[0]
# ====================简介====================
raw_description = tree.xpath('//section[@class="item-description"]/text()')  # 列表
description = "".join(raw_description)
format_description = description.replace("\n", "|")

# ====================价格====================
price = tree.xpath('//h5[@class="item-price"]/text()')[0]
# ====================评星====================
review_count = tree.xpath('//div[@itemprop="reviewCount"]/text()')[0]
# ====================创作信息====================
credit_list = []
raw_credits = tree.xpath('//div[@class="credits"]/*/text()')  # 列表
for i in range(len(raw_credits)):
    credit_line = raw_credits[i].strip("\t\n")
    if credit_line != "":
        credit_list.append(credit_line)
credit = "\n".join(credit_list)
print(len(credit))

# ========================输出区开始========================
info_list = ("标题: " + title, "价格: " + price, "简介: " + description, "创作信息: " + "\n" + credit, "评星: " + review_count)
info = "\r\n".join(info_list)
print(info)

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
