from lxml import html
import requests, urllib.parse, time, os

start_time = time.time()  # 初始时间戳


def GetMagnet(user):
    # ========================输入区开始========================

    defualt_page_count = 20

    output_file_name = "thepiratebay-用户" + user + '地址.csv'  # 文件名
    search_domain = 'https://thepiratebay.org/user/'  # 搜索的网站地址
    dropbox_path = '/Users/alicewish/Dropbox'  # 文件地址前缀
    output_file_path = os.path.join(dropbox_path, output_file_name)

    # ========================执行区开始========================

    output_readline = []

    # ==================获取总页数==================
    test_url = 'https://thepiratebay.org/user/' + user
    this_page = requests.get(test_url)  # 第1页

    tree = html.fromstring(this_page.text)
    title_list = tree.xpath('//a[@class="detLink"]/text()')
    magnet_list = tree.xpath('//a[@title="Download this torrent using magnet"]/@href')

    count = len(title_list)
    for i in range(count):
        output_line_in_list = [title_list[i], magnet_list[i]]
        output_line = ",".join(output_line_in_list)
        output_readline.append(output_line)

    # ================写入文本================
    text = '\r\n'.join(output_readline)
    print(text)

    f = open(output_file_path, 'w')
    try:
        f.write(text)
    finally:
        f.close()


GetMagnet('shipjolly')
