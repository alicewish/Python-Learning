import time, re
from lxml import html

start_time = time.time()  # 初始时间戳

# ==============读取文本==============
input_file_path = '/Users/alicewish/Downloads/百度云 网盘-我的分享.htm'
read_text = open(input_file_path, 'r').read()  # 读取文本
tree = html.fromstring(read_text)

# ==============读取文件名==============
names = tree.xpath('//span[@node-type="name-text"]/@title')  # 列表存储
all_name = '\n'.join(names)
print(len(names))
print(all_name)

# ==============读取下载地址==============
share_links = []
links = tree.xpath('//a[@target="_blank"]/@href')  # 列表存储
for link in links:
    if re.match(r'http://pan.baidu.com/s/[^<]*', link):  # 判断是否度盘外链
        share_links.append(link)
all_link = '\n'.join(share_links)
print(len(share_links))
print(all_link)

# ==============读取分享时间和浏览、保存、下载次数==============
raw_share_time = tree.xpath('//div[@style="width: 20%"]/text()')  # 列表存储分享时间
all_number = tree.xpath('//div[@style="width: 9%"]/text()')  # 列表存储各类次数

share_time=[]
view_number=[]
save_number=[]
download_number=[]
for i in range(len(names)):
    share_time.append(raw_share_time[i+1].strip(" \n\t\r"))
    view_number.append(all_number[3*i+3].strip(" \n\t\r")) # 浏览次数
    save_number.append(all_number[3*i+4].strip(" \n\t\r")) # 保存次数
    download_number.append(all_number[3*i+5].strip(" \n\t\r")) # 下载次数

# ==============合并信息==============
info_list=[]
if len(names)==len(share_links):
  for i in range(len(names)):
    info=names[i]+"\t"+share_links[i]+"\t"+share_time[i]+"\t"+view_number[i]+"\t"+save_number[i]+"\t"+download_number[i]
    info_list.append(info)
else:
  print("错误")
all_info = '\n'.join(info_list)

print(all_info)
# ================写入剪贴板================
import pyperclip
pyperclip.copy(all_info)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
