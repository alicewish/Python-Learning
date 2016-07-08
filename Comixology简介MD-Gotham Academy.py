from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================
search_comic_name = 'Gotham Academy'  # 查询用漫画名
issue_name_prefix = 'Gotham Academy (2014-)'
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
issues_info = {}
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
            issues_info[title] = format_description  # 写入字典

            line_info = ["### " + title, format_description]
            this_line = "\r\n".join(line_info)
            print(this_line)

            entry_run_time = time.time() - entry_start_time
            print("耗时:{:.2f}秒".format(entry_run_time))
        else:
            check_set.add(short_link)

# ========================输出区开始========================
out_info = []
for i in range(1, len(issues_url)):
    key = issue_name_prefix + " #"+str(i)
    if key in issues_info:
        try:
            out_info.append("### " + key)
            out_info.append(issues_info[key])
        except:
            pass

out_text = "\r\n".join(out_info)

# ================写入TXT================
txt_file_path = '/Users/alicewish/我的坚果云/Comixology简介MD-' + save_comic_name + '.txt'  # TXT文件名
f = open(txt_file_path, 'w')
try:
    f.write(out_text)
finally:
    f.close()
# ================写入剪贴板================
import pyperclip

pyperclip.copy(out_text)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
