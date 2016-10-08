from lxml import html
import requests, urllib.parse, time

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================
search_term = '0 Day Week'  # 搜索的关键词
file_name = '0-Day Week地址-' + now  # 文件名

search_order = '/?field=time_add&sorder=desc'  # 搜索的顺序
search_domain = 'https://kat.cr/usearch/'  # 搜索的网站地址
path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名
excel_file_path = path_prefix + file_name + '.xls'  # XLS文件名

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
# ==================显示页数和项数==================
print("一共有" + str(page_number) + "页," + str(entry_length) + "项")
# ==================遍历网页==================
# ================外循环:读取页面================
for i in range(page_number):
    page_start_time = time.time()
    thispage = requests.get(search_domain + search_term + '/' + str(i + 1) + search_order)
    tree = html.fromstring(thispage.text)
    dataparams = tree.xpath('//div[@class="none"]/@data-sc-params')
    # data-sc-params形如{ 'name': '...', 'extension': 'cbr', 'magnet': '...' }
    cell_link = tree.xpath('//a[@class="normalgrey font12px plain bold"]/@href')
    # href形如"/[...].html"
    # ==============内循环:读取每页项目==============
    for j in range(25):
        try:
            entry_start_time = time.time()
            data = eval(dataparams[j])  # 将字符串转化成字典dict类型,设为data
            link = cell_link[j]  # 相对链接的字符串
            full_link = "https://kat.cr" + link

            name = urllib.parse.unquote(data['name'])  # 获取文件名
            extension = urllib.parse.unquote(data['extension'])  # 获取拓展类型
            magnet = urllib.parse.unquote(data['magnet'])  # 获取磁力链接

            info = (name, magnet, '')  # 将信息设成格式为(文件名,磁力链接,'')的元组
            text = '\r\n'.join(info)  # 将文本设为信息断行拼合
            # ============操作TXT============
            f = open(txt_file_path, 'a')
            try:
                f.write(text)
            finally:
                f.close()

            # ================每项时间计时================
            entry_run_time = time.time() - entry_start_time
            entry_print = "第" + str(i + 1) + "页" + "第" + str(j + 1) + "项读取中\n链接为:" + full_link + "\n耗时:{:.4f}秒".format(
                entry_run_time)
            print(entry_print)
        except:
            print("本页已经读取完成")
    # ================每页时间计时================
    page_run_time = time.time() - page_start_time
    page_print = "第" + str(i + 1) + "页读取完毕," + "耗时:{:.4f}秒".format(page_run_time)
    print(page_print)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
