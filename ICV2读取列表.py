import requests, time, os
from lxml import html

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
main_url = "http://icv2.com/articles/news/view/1850/"  # 完整文章网址

now_date = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳

dropbox_path = '/Users/alicewish/Dropbox'

output_readline = []
# ========================执行区开始========================
page = requests.get(main_url)
tree = html.fromstring(page.text)
# ====================获取本页名称====================
article_title = tree.xpath("//title/text()")[0]  # 文章名称

# ====================获取新文章列表====================
new_article_title_list = tree.xpath("//div[@class='article-text clearfix mrl5']/p/a/text()")  # 以列表形式存储的新文章名称列表
new_article_url_list = tree.xpath("//div[@class='article-text clearfix mrl5']/p/a/@href")  # 以列表形式存储的新文章地址列表
# ====================获取旧文章列表====================
old_article_title_list = tree.xpath("//div[@class='article-text clearfix mrl5']/a/text()")  # 以列表形式存储的旧文章名称列表
old_article_url_list = tree.xpath("//div[@class='article-text clearfix mrl5']/a/@href")  # 以列表形式存储的旧文章地址列表
# ====================合并文章列表====================
article_title_list = new_article_title_list + old_article_title_list  # 以列表形式存储的总文章名称列表
article_url_list = new_article_url_list + old_article_url_list  # 以列表形式存储的总文章地址列表
article_title_list_length = len(article_title_list)  # 总文章数


def csvconvert(string):
    converted_string = string.replace('"', '""')
    return converted_string


info = ""  # 初始化信息字符串为空
for i in range(article_title_list_length):
    info += article_title_list[i] + "\n"
    info += article_url_list[i] + "\n"
    output_line_in_list = [csvconvert(article_title_list[i]), csvconvert(article_url_list[i])]
    output_line = '"' + '","'.join(output_line_in_list) + '"'
    output_readline.append(output_line)

print(article_title)
print(main_url)
print(info)
print(article_title_list_length)

text = '\r\n'.join(output_readline)

# ================写入CSV================

output_file_name = article_title.replace("ICv2: ", "") + '.csv'

output_file_path = os.path.join(dropbox_path, output_file_name)
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
