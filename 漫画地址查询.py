from lxml import html
import requests, urllib.parse, time, xlwt, xlrd

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================
file_name = '漫画包磁力链接' + now  # 文件名

search_order = '/?field=time_add&sorder=desc'  # 搜索的顺序
search_domain = 'https://kat.cr/usearch/'  # 搜索的网站地址
path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名

# ========================执行区开始========================
# ==================0 Day Week==================
search_term = '0 Day Week'  # 搜索的关键词
# ================读取第一页================
page_start_time = time.time()
thispage = requests.get(search_domain + search_term + '/' + str(1) + search_order)
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
        entry_print = "第1页" + "第" + str(j + 1) + "项读取中\n链接为:" + full_link + "\n耗时:{:.4f}秒".format(
            entry_run_time)
        print(entry_print)
    except:
        print("本页已经读取完成")
# ================每页时间计时================
page_run_time = time.time() - page_start_time
page_print = "第1页读取完毕," + "耗时:{:.4f}秒".format(page_run_time)
print(page_print)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
