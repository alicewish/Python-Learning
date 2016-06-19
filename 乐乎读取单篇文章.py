from lxml import html
import requests, urllib.parse, time, xlwt, xlrd, html2text

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
user_hash = '38ea7d'  # 用户Hash
post_hash = 'b523a2f'  # 文章Hash
file_name = '乐乎文章'

url_prefix = 'http://underdream.lofter.com/post/'  # 网址前缀
full_url = url_prefix + user_hash + '_' + post_hash
path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名

# ========================执行区开始========================
# # ==================操作TXT==================
# f = open(txt_file_path, 'w')
# text = search_term + " Full List\r\n"  # 写入标题
# try:
#     f.write(text)
# finally:
#     f.close()

# ==================获取文章==================
thispage = requests.get(full_url)  # 文章页
# tree = html.fromstring(thispage.text)
# dataparams = tree.xpath('//a[@class="turnoverButton siteButton bigButton"]/text()')
# page_number = int(dataparams[-1])  # 总页数
print(html2text.html2text(thispage.text)) #以Markdown格式显示

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
