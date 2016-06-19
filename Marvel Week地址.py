from lxml import html
import requests, urllib.parse, time, xlwt, xlrd

start_time = time.time()  # 时间戳
# ========================输入区开始========================
search_term = 'Marvel Week'  # 搜索的关键词
path_prefix = '/Users/alicewish/我的坚果云/'  # 地址前缀
txt_file_path = path_prefix + 'Marvel Week地址.txt'  # TXT文件名
excel_file_path = path_prefix + 'Marvel Week地址.xlsx'  # XLSX文件名
# ========================执行区开始========================
# ==================操作TXT==================
f = open(txt_file_path, 'w')
text = search_term + " Full List\r\n"  # 写入标题
try:
    f.write(text)
finally:
    f.close()
# ==================操作EXCEL==================
data = xlrd.open_workbook(excel_file_path)  # 读取EXCEL
workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook
worksheet = workbook.add_sheet(search_term)  # 创建名为搜索的关键词的表
worksheet.write(0, 0, label='文件名称')  # 往单元格内写入内容
worksheet.write(0, 1, label='磁力链接')  # 往单元格内写入内容
workbook.save(excel_file_path)  # 保存EXCEL
# ==================获取总页数==================
thispage = requests.get('https://kat.cr/usearch/' + search_term + '/1/?field=time_add&sorder=desc')
tree = html.fromstring(thispage.text)
dataparams = tree.xpath('//a[@class="turnoverButton siteButton bigButton"]/text()')
page_number = int(dataparams[-1])  # 总页数
# ==================遍历网页==================
# ================外循环:================
for i in range(1, page_number):
    thispage = requests.get('https://kat.cr/usearch/' + search_term + '/' + str(i) + '/?field=time_add&sorder=desc')
    tree = html.fromstring(thispage.text)
    dataparams = tree.xpath('//div[@class="none"]/@data-sc-params') #dataparams是
    # ==============内循环==============
    for j in range(0, 24):
        data = eval(dataparams[j])  # 将字符串转化成字典dict类型

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
        # ==================操作EXCEL==================
        data = xlrd.open_workbook(excel_file_path)  # 读取EXCEL
        workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook
        worksheet = workbook.add_sheet(search_term)  # 创建名为搜索的关键词的表
        worksheet.write(0, 0, label='文件名称')  # 往单元格内写入内容
        worksheet.write(0, 1, label='磁力链接')  # 往单元格内写入内容
        workbook.save(excel_file_path)  # 保存EXCEL

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:
    print("耗时: {:.2f}秒".format(run_time))
elif run_time < 3600:
    print("耗时: {:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:
    print("耗时: {:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
