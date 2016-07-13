from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# # ========================输入区开始========================
# input_file_name = '微博UID'  # 输入文件的名称
output_file_name = '微博信息批量获取'  # 输出文件的名称
#
path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
# input_file_path = path_prefix + input_file_name + '.txt'  # 输入文件的地址
output_file_path = path_prefix + output_file_name + '.txt'  # 输出文件的地址

# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()
text_readline = read_text.splitlines()
print(text_readline)
# ========================处理文本========================
nickname_list = []  # 初始化昵称列表
friends_list = []  # 初始化好友数列表
fans_list = []  # 初始化粉丝数列表
posts_list = []  # 初始化微博数列表
info_list = []  # 初始化信息列表

for i in range(len(text_readline)):
    entry_start_time = time.time()
    # ========================获取昵称和粉丝数========================
    nickname = ""
    friends = ""
    fans = ""
    posts = ""
    location = ""
    description = ""
    days = ""
    started = ""
    try:
        page = requests.get('http://sinacn.weibodangan.com//user/' + text_readline[i])
        tree = html.fromstring(page.text)
        nickname = tree.xpath('//h3[@class="username"]/text()')[0]
        data = tree.xpath('//td/text()')
        friends = data[0]
        fans = data[1].replace(" ", "")
        posts = data[2]
        alldays = tree.xpath("//div[@class='hidden-xs hidden-sm']/p[1]/text()")[0]
        days = alldays[7:]
        started = tree.xpath("//span[@id='register_time']/text()")[0]
        location = tree.xpath("//div[@class='info'][1]/text()")[0]
        description = tree.xpath("//div[@class='info'][2]/text()")[0]
    except:
        pass
    info = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\t" + nickname + "\t" + friends + "\t" + fans + "\t" + posts + "\t" + location + "\t" + description + "\t" + days + "\t" + started
    info_list.append(info)
    # ================每项时间计时================
    entry_run_time = time.time() - entry_start_time
    entry_print = "耗时:{:.4f}秒".format(entry_run_time)
    print(info_list[i], "\n", entry_print)

# ================写入昵称列表================
text = '\r\n'.join(info_list)  # 写入文本
# ================写入剪贴板================
import pyperclip

pyperclip.copy(text)
spam = pyperclip.paste()

# ================写入文本文档================
f = open(output_file_path, 'w')
try:
    f.write(text)
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
