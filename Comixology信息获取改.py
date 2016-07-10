from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================
comic_name = 'Batman-2016-1'  # 查询用漫画名
comic_ID = "366119"  # 查询用漫画ID

url_prefix = 'https://www.comixology.com/'
url_middle = '/digital-comic/'
comic_url = url_prefix + comic_name + url_middle + comic_ID  # 完整的查询网址
print(comic_url)

short_link = "https://www.comixology.com/Batman-2016-7/digital-comic/397853"
key_word_list = ["Written by", "Art by", "Pencils", "Inks", "Cover by", "Genres", "Print Release Date",
                 "Print Release Date", "Page Count", "Age Rating", "Sold by"]
# ========================执行区开始========================
page = requests.get(short_link)  # 获取网页信息
tree = html.fromstring(page.text)  # 构筑查询用树
# ====================标题====================
title = tree.xpath('//h2[@class="title"]/text()')[0]
# ====================简介====================
raw_description = tree.xpath('//section[@class="item-description"]/text()')  # 列表
description = "".join(raw_description)
format_description = description.strip("\n\t").replace("\r\n", "|").replace("\r", "|").replace("\n", "|")
# ====================创作信息====================
credit_list = []
raw_credits = tree.xpath('//div[@class="credits"]//*/text()')  # 列表
for i in range(len(raw_credits)):
    credit_line = raw_credits[i].strip("\t\n")
    if credit_line != "" and credit_line != "HIDE...":
        credit_list.append(credit_line)
credit = "\n".join(credit_list)

# ====================评价数====================
rating_count = ""
try:
    review_count = tree.xpath('//div[@itemprop="reviewCount"]/text()')[0]
    rating_count = review_count.replace("Average Rating (", "").replace("):", "")
except:
    pass
# ====================编剧====================
writer = ""
item = "Written by"
if item in credit_list:
    item_index = credit_list.index(item)
    temp_store = credit_list[item_index + 1]
    while credit_list[item_index + 2] not in key_word_list:
        item_index += 1
        temp_store = temp_store + "|" + credit_list[item_index + 1]
    writer = temp_store
# ====================画师====================
artist = ""
item = "Art by"
if item in credit_list:
    item_index = credit_list.index(item)
    temp_store = credit_list[item_index + 1]
    while credit_list[item_index + 2] not in key_word_list:
        item_index += 1
        temp_store = temp_store + "|" + credit_list[item_index + 1]
    artist = temp_store
# ====================铅稿====================
penciller = ""
item = "Pencils"
if item in credit_list:
    item_index = credit_list.index(item)
    temp_store = credit_list[item_index + 1]
    while credit_list[item_index + 2] not in key_word_list:
        item_index += 1
        temp_store = temp_store + "|" + credit_list[item_index + 1]
    penciller = temp_store
# ====================墨线====================
inker = ""
item = "Inks"
if item in credit_list:
    item_index = credit_list.index(item)
    temp_store = credit_list[item_index + 1]
    while credit_list[item_index + 2] not in key_word_list:
        item_index += 1
        temp_store = temp_store + "|" + credit_list[item_index + 1]
    inker = temp_store
# ====================封面====================
cover_artist = ""
item = "Cover by"
if item in credit_list:
    item_index = credit_list.index(item)
    temp_store = credit_list[item_index + 1]
    while credit_list[item_index + 2] not in key_word_list:
        item_index += 1
        temp_store = temp_store + "|" + credit_list[item_index + 1]
    cover_artist = temp_store
# ====================类型====================
genres = ""
item = "Genres"
if item in credit_list:
    item_index = credit_list.index(item)
    temp_store = credit_list[item_index + 1]
    while credit_list[item_index + 2] not in key_word_list:
        item_index += 1
        temp_store = temp_store + "|" + credit_list[item_index + 1]
    genres = temp_store
# ====================数字出版日期====================
digital_release_date = ""
item = "Digital Release Date"
if item in credit_list:
    time_string = credit_list[credit_list.index(item) + 1]
    time_convert = time.strptime(time_string, "%B %d %Y")
    digital_release_date = time.strftime("%Y-%m-%d", time_convert)
# ====================实体出版日期====================
print_release_date = ""
item = "Print Release Date"
if item in credit_list:
    time_string = credit_list[credit_list.index(item) + 1]
    time_convert = time.strptime(time_string, "%B %d %Y")
    print_release_date = time.strftime("%Y-%m-%d", time_convert)
# ====================页数====================
page_count = ""
item = "Page Count"
if item in credit_list:
    page_count = (credit_list[credit_list.index(item) + 1]).replace(" Pages", "")
# ====================年龄评级====================
age_rating = ""
item = "Age Rating"
if item in credit_list:
    age_rating = (credit_list[credit_list.index(item) + 1]).replace(" Only", "")
# ====================出版公司====================
publisher = ""
item = "Sold by"
if item in credit_list:
    publisher = credit_list[credit_list.index(item) + 1]
# ====================输出区开始====================
line_info = [title, short_link, format_description, digital_release_date, page_count, age_rating,
             rating_count, publisher, genres, writer, artist, penciller, inker, cover_artist]
this_line = "\t".join(line_info)  # 行信息合并
print(this_line)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
