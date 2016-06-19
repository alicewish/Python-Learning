from lxml import html
import requests, urllib.parse, time, xlwt, xlrd

# ========================输入区开始========================
search_term = 'Marvel Week'  # 搜索的关键词
search_order = '/?field=time_add&sorder=desc'  # 搜索的顺序
search_domain = 'https://kat.cr/usearch/'  # 搜索的网站地址
path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + 'Marvel Week地址.txt'  # TXT文件名
excel_file_path = path_prefix + 'Marvel Week地址.xls'  # XLS文件名

# ========================执行区开始========================
# ==================获取总页数==================
thispage = requests.get(search_domain + search_term + '/1' + search_order)  # 第1页
tree = html.fromstring(thispage.text)
dataparams = tree.xpath('//a[@class="turnoverButton siteButton bigButton"]/text()')
page_number = int(dataparams[-1])  # 总页数
# ==================获取最后一页项数==================
thispage = requests.get(search_domain + search_term + '/' + str(page_number) + search_order)
tree = html.fromstring(thispage.text)
dataparams = tree.xpath('//div[@class="none"]/@data-sc-params')
last_page_entry = len(dataparams)  # 最后一页项数
# ==================计算总项数==================
entry_length = (page_number - 1) * 25 + last_page_entry  # 总项数
print("一共有" + str(entry_length) + "项")
# ==================遍历网页==================
# ================外循环:读取页面================
for i in range(page_number):
    page_start_time = time.time()
    thispage = requests.get(search_domain + search_term + '/' + str(i + 1) + search_order)
    tree = html.fromstring(thispage.text)

    cell_link = tree.xpath('//div[@class="markeredBlock torType pdfType"]/a[@class="cellMainLink"]/@href')
    print(cell_link)


