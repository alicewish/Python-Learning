
import  time,  MyDef

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳


def ComixIssue(search_comic_name="Transformers"):
    from lxml import html
    import requests, time, re
    # ========================输入区开始========================
    save_comic_name = search_comic_name.replace(":", "").replace("/", "").replace("&", "").replace("  ", " ")
    key_title = search_comic_name.replace(" ", "-")
    print(key_title)
    url_prefix = 'https://www.comixology.com/search?search='
    comic_url = url_prefix + search_comic_name  # 完整的查询网址
    # ========================执行区开始========================
    page = requests.get(comic_url)  # 获取网页信息
    tree = html.fromstring(page.text)  # 构筑查询用树
    # ====================找到系列====================
    all_url = tree.xpath('//a[@class="content-details"]/@href')
    print(len(all_url))

    issues_url = []  # 每期网址
    check_set = set()  # 重复检查
    info_dict = {}
    alter_info_dict = {}
    major_key_list = []
    for i in range(len(all_url)):
        entry_start_time = time.time()
        print(i)
        print(all_url[i])
        if re.match(r'.*/digital-comic/[^?]*', all_url[i]) and key_title in all_url[i]:
            matches = re.match(r'.*/digital-comic/[^?]*', all_url[i])
            short_link = matches.group(0)
            if short_link not in check_set:  # 尚未读取过
                check_set.add(short_link)
                print("获取中……")
                issues_url.append(short_link)
                # ========================执行区开始========================
                page = requests.get(short_link)  # 获取网页信息
                tree = html.fromstring(page.text)  # 构筑查询用树
                # ====================关键词列表====================
                key_word_list = ["Written by", "Art by", "Pencils", "Inks", "Colored by", "Cover by", "Genres",
                                 "Digital Release Date", "Print Release Date", "Page Count", "Age Rating", "Sold by",
                                 "About Book"]
                # ====================标题====================
                title = tree.xpath('//h1[@class="title"]/text()')[0]
                # ====================简介====================
                raw_description = tree.xpath('//section[@class="item-description"]/text()')  # 列表
                description = "".join(raw_description)
                formatted_description = description.strip("\n\t").replace("\r\n", "|")
                formatted_description = formatted_description.replace("\r", "|").replace("\n", "|")
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
                # ====================价格====================
                price = ""
                try:
                    price = tree.xpath('//h5[@class="item-price"]/text()')[0]
                except:
                    pass
                # ====================封面====================
                cover_image_url = ""
                try:
                    cover_image_url = tree.xpath('//img[@class="cover"]/@src')[0]
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
                # ====================上色====================
                colorist = ""
                item = "Colored by"
                if item in credit_list:
                    item_index = credit_list.index(item)
                    temp_store = credit_list[item_index + 1]
                    while credit_list[item_index + 2] not in key_word_list:
                        item_index += 1
                        temp_store = temp_store + "|" + credit_list[item_index + 1]
                    colorist = temp_store
                # ====================填字====================
                letterer = ""
                item = "Lettered by"
                if item in credit_list:
                    item_index = credit_list.index(item)
                    temp_store = credit_list[item_index + 1]
                    while credit_list[item_index + 2] not in key_word_list:
                        item_index += 1
                        temp_store = temp_store + "|" + credit_list[item_index + 1]
                    letterer = temp_store
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
                # ====================故事线====================
                story_arc = ""
                item = "Story Arc"
                if item in credit_list:
                    item_index = credit_list.index(item)
                    temp_store = credit_list[item_index + 1]
                    while credit_list[item_index + 2] not in key_word_list:
                        item_index += 1
                        temp_store = temp_store + "|" + credit_list[item_index + 1]
                    story_arc = temp_store
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
                line_info = [title, digital_release_date, print_release_date, price,
                             page_count, age_rating, rating_count, publisher, genres, story_arc, writer, artist,
                             penciller, inker, colorist, letterer, cover_artist, short_link, cover_image_url,
                             formatted_description]
                this_line = "\t".join(line_info)  # 行信息合并
                print(this_line)

                major_key = digital_release_date + title  # "日期+标题"作为主键
                major_key_list.append(major_key)
                info_dict[major_key] = line_info
                major_key_list.sort()  # 主键表排序
                text_list = []
                for key in major_key_list:
                    text_list.append(info_dict[key])

                # ================写入TXT================
                txt_file_path = '/Users/alicewish/Dropbox/Comixology刊物' + save_comic_name + '.csv'  # TXT文件名
                head_info = ["标题", "数字出版日期", "实体出版日期", "价格", "页数", "分级", "评价数", "出版商", "类型", "故事线", "编剧", "画师", "铅笔稿",
                             "墨线", "上色师", "填字员", "封面画师", "短链", "封面图地址", "简介"]
                MyDef.StoreCSV(text_list, txt_file_path,head_info)

                # ====================次级输出区开始====================
                alter_line_info = ["### " + title, formatted_description]
                alter_line = "\r\n".join(alter_line_info)  # 行信息合并
                print(alter_line)

                alter_info_dict[major_key] = alter_line
                major_key_list.sort()  # 主键表排序
                alter_text_list = []
                for key in major_key_list:
                    alter_text_list.append(alter_info_dict[key])

                alter_text = "\r\n".join(alter_text_list)
                # ================写入TXT================
                alter_txt_file_path = '/Users/alicewish/我的坚果云/Comixology简介' + save_comic_name + '.txt'  # TXT文件名
                f = open(alter_txt_file_path, 'w')
                try:
                    f.write(alter_text)
                finally:
                    f.close()

                entry_run_time = time.time() - entry_start_time
                print("耗时:{:.2f}秒".format(entry_run_time))

    # ========================输出区开始========================
    print("总共" + str(len(issues_url)) + "期")


ComixIssue(search_comic_name="Tomboy")
print("总耗时:", MyDef.RunTime(start_time))
