from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================
search_comic_name = 'Bombshells'  # 查询用漫画名

save_comic_name = search_comic_name.replace(":", "").replace("+", "").replace("  ", " ")
key_title = save_comic_name.replace(" ", "-")
print(key_title)
url_prefix = 'https://www.comixology.com/search?search='
comic_url = url_prefix + search_comic_name  # 完整的查询网址
# ========================执行区开始========================
page = requests.get(comic_url)  # 获取网页信息
tree = html.fromstring(page.text)  # 构筑查询用树
# ====================找到系列====================
all_url = tree.xpath('//a[@class="content-details"]/@href')
print(len(all_url))

issues_url = []
check_set = set()
info_dict = {}
major_key_list = []
for i in range(len(all_url)):
    entry_start_time = time.time()
    print(i)
    print(all_url[i])
    if re.match(r'.*/digital-comic/[^?]*', all_url[i]) and key_title in all_url[i]:
        matchs = re.match(r'.*/digital-comic/[^?]*', all_url[i])
        short_link = matchs.group(0)
        if short_link not in check_set:
            check_set.add(short_link)
            print("获取中……")
            issues_url.append(short_link)
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
                writer = credit_list[credit_list.index(item) + 1]
            # ====================铅稿====================
            artist = ""
            item = "Art by"
            if item in credit_list:
                artist = credit_list[credit_list.index(item) + 1]
            # ====================铅稿====================
            penciller = ""
            item = "Pencils"
            if item in credit_list:
                penciller = credit_list[credit_list.index(item) + 1]
            # ====================墨线====================
            inker = ""
            item = "Inks"
            if item in credit_list:
                inker = credit_list[credit_list.index(item) + 1]
            # ====================封面====================
            cover_artist = ""
            item = "Cover by"
            if item in credit_list:
                cover_artist = credit_list[credit_list.index(item) + 1]
            # ====================类型====================
            genres = ""
            item = "Genres"
            if item in credit_list:
                genres = credit_list[credit_list.index(item) + 1]
            # ====================数字出版日期====================
            digital_release_date = ""
            item = "Digital Release Date"
            if item in credit_list:
                time_string = credit_list[credit_list.index(item) + 1]
                time_convert = time.strptime(time_string, "%B %d %Y")
                digital_release_date = time.strftime("%Y-%m-%d", time_convert) \
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
            line_info = ["### "+title,  format_description]
            this_line = "\r\n".join(line_info)  # 行信息合并
            print(this_line)

            major_key = digital_release_date + title  # "日期+标题"作为主键
            major_key_list.append(major_key)
            info_dict[major_key] = this_line
            major_key_list.sort()  # 主键表排序
            text_list = []
            for key in major_key_list:
                text_list.append(info_dict[key])

            text = "\r\n".join(text_list)
            # ================写入TXT================
            txt_file_path = '/Users/alicewish/我的坚果云/Comixology简介MD-' + save_comic_name + '.txt'  # TXT文件名
            f = open(txt_file_path, 'w')
            try:
                f.write(text)
            finally:
                f.close()
            entry_run_time = time.time() - entry_start_time
            print("耗时:{:.2f}秒".format(entry_run_time))

# ========================输出区开始========================
print("总共"+len(issues_url)+"期")

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
