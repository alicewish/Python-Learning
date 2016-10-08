from lxml import html
import requests, urllib.parse, time, os, MyDef

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
this_week_readline = []
# ==============================shipjolly==============================
user = 'nemesis43'  # 用户名

defualt_page_count = 20

output_file_name = "thepiratebay-用户" + user + '地址.csv'  # 文件名
search_domain = 'https://thepiratebay.org/user/'  # 搜索的网站地址
dropbox_path = '/Users/alicewish/Dropbox'  # 文件地址前缀
output_file_path = os.path.join(dropbox_path, output_file_name)

# ========================执行区开始========================

output_readline = []

# ==================获取总页数==================
test_url = 'https://thepiratebay.org/user/'+user
this_page = requests.get(test_url)  # 第1页

tree = html.fromstring(this_page.text)
title_list = tree.xpath('//a[@class="detLink"]/text()')
magnet_list = tree.xpath('//a[@title="Download this torrent using magnet"]/@href')

count = len(title_list)
for i in range(count):
    output_line_in_list = [title_list[i], magnet_list[i]]
    output_line = ",".join(output_line_in_list)
    output_readline.append(output_line)

this_week_readline.append(magnet_list[0])
this_week_readline.append(magnet_list[1])
# ================写入文本================
text = '\r\n'.join(output_readline)
print(text)

f = open(output_file_path, 'w')
try:
    f.write(text)
finally:
    f.close()


info = "\r\n".join(this_week_readline)
print(info)
print(len(this_week_readline))

MyDef.Clipboard(info)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
