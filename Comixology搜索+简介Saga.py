from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================
search_comic_name = 'Saga'  # 查询用漫画名

save_comic_name = search_comic_name.replace(":", "")
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
all_info = []
check_set = set()
for i in range(len(all_url)):
    entry_start_time = time.time()
    print(i)
    print(all_url[i])
    if re.match(r'.*/digital-comic/[^?]*', all_url[i]) and key_title in all_url[i]:
        matchs = re.match(r'.*/digital-comic/[^?]*', all_url[i])
        short_link = matchs.group(0)
        if short_link not in check_set:
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
            raw_credits = tree.xpath('//div[@class="credits"]/*/text()')  # 列表
            for i in range(len(raw_credits)):
                credit_line = raw_credits[i].strip("\t\n")
                if credit_line != "":
                    credit_list.append(credit_line)
            credit = "\n".join(credit_list)
            print(len(credit))

            digital_release_date = ""
            for i in range(len(credit_list)):
                if credit_list[i] == "Digital Release Date":
                    digital_release_date = credit_list[i + 1]

            line_info = [short_link, title, format_description, digital_release_date]
            this_line = "\t".join(line_info)
            print(this_line)
            all_info.append(this_line)
            text = '\r\n'.join(all_info)
            # ================写入TXT================
            txt_file_path = '/Users/alicewish/我的坚果云/Comixology搜索+简介' + save_comic_name + '.txt'  # TXT文件名
            f = open(txt_file_path, 'w')
            try:
                f.write(text)
            finally:
                f.close()
            entry_run_time = time.time() - entry_start_time
            print("耗时:{:.2f}秒".format(entry_run_time))
        else:
            check_set.add(short_link)

# ========================输出区开始========================
print(len(issues_url))

# ================写入剪贴板================
import pyperclip

pyperclip.copy(text)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))