# ================运行时间计时================
def RunTime(start_time):
    import time
    run_time = time.time() - start_time
    if run_time < 60:  # 两位小数的秒
        show_run_time = "{:.2f}秒".format(run_time)
    elif run_time < 3600:  # 分秒取整
        show_run_time = "{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60)
    else:  # 时分秒取整
        show_run_time = "{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60)
    return show_run_time


# ================存储到CSV================
def StoreCSV(list, path, head_info='', system='Mac'):
    # ================格式化文本================
    if head_info != '':
        list.insert(0, head_info)
    output_readline = []
    for output_line_in_list in list:
        element_list = []
        for element in output_line_in_list:
            element = element.replace('"', '""')
            element_list.append(element)
        output_line = '"' + '","'.join(element_list) + '"'
        output_readline.append(output_line)

    text = '\r\n'.join(output_readline)
    if system == 'Mac':
        # ================写入CSV================
        f = open(path, 'w')
        try:
            f.write(text)
        finally:
            f.close()
    else:
        # ================写入CSV================
        f = open(path, 'wb')
        try:
            f.write(text.encode('gb2312'))
        finally:
            f.close()


# ================读取CSV到列表================
def ReadCSV(path, type=False):
    text_readline = []  # 初始化按行存储数据列表
    with open(path) as fin:
        for line in fin:
            line = line.strip("\r\n")[1:-1]
            line_list = line.split('","')
            text_readline.append(line_list)
    if type:
        text_readline.pop(0)
    return text_readline


# ================读取剪贴板================
def ReadClip():
    from tkinter import Tk
    r = Tk()
    read_text = r.clipboard_get()
    return read_text


# ================读取剪贴板并分行================
def ReadClipL():
    from tkinter import Tk
    r = Tk()
    read_text = r.clipboard_get()
    text_readline = read_text.splitlines()
    return text_readline


# ================写入剪贴板================
def WriteClip(info):
    import pyperclip
    pyperclip.copy(info)
    spam = pyperclip.paste()
    return spam


# ================按行读取文本================
def ReadText(path):
    text_readline = []  # 初始化按行存储数据列表
    with open(path) as fin:
        for line in fin:
            text_readline.append(line.strip("\r\n"))
    return text_readline


# ================获取文件夹大小================
def GetFolderSize(path):
    import os
    from os.path import join, getsize
    TotalSize = 0
    for item in os.walk(path):
        for file in item[2]:
            try:
                TotalSize = TotalSize + getsize(join(item[0], file))
            except:
                print("文件遇到错误:  " + join(item[0], file))
    return TotalSize


# ================获取文件时间信息================
def FileTime(path):
    import os, datetime
    last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(path))  # 最近访问时间
    created_time = datetime.datetime.fromtimestamp(os.path.getctime(path))  # 输出文件创建时间
    last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(path))  # 最近修改时间
    return [last_access_time, created_time, last_modified_time]


# ================读取TXT字典================
def ReadDictA(refer_file_path):
    refer_dict = {}
    with open(refer_file_path) as fin:
        for line in fin:
            refer_line = (line.replace('\n', '')).replace('\t', '')
            if "|" in refer_line:  # 接受key|value格式
                split_line_list = refer_line.split("|")
                refer_dict[split_line_list[0]] = split_line_list[1]
    return refer_dict


# ================读取CSV字典================
def ReadDictB(refer_file_path):
    refer_dict = {}
    with open(refer_file_path) as fin:
        for line in fin:
            line = line.strip("\r\n")[1:-1]
            line_list = line.split('","')
            refer_dict[line_list[0]] = line_list[1]
    return refer_dict


# ================读取CSV字典================
def ReadDictC(refer_file_path, type=False):
    refer_dict = {}
    if type:
        status = True
    else:
        status = False
    with open(refer_file_path) as fin:
        for line in fin:
            if status:
                status = False
            else:
                line = line.strip("\r\n")[1:-1]
                line_list = line.split('","')
                refer_dict[line_list[0]] = line_list[1]
    return refer_dict


# ================存储CSV字典================
def WriteDictB(refer_dict, refer_file_path):
    key_list = []
    for key in refer_dict:
        key_list.append(key)
    key_list.sort()
    dict_list = []
    for key in key_list:
        value = refer_dict[key]
        dict_list.append([key, value])
    StoreCSV(dict_list, refer_file_path)


# ================CSV格式规范================
def CSVConvert(string):
    converted_string = string.replace('"', '""')
    return converted_string


# ================使用正则表达式匹配文本，获得全部匹配结果================
def ReFind(text, re_pattern):
    import re
    pattern = re.compile(re_pattern)
    # ================使用Pattern匹配文本，获得全部匹配结果================
    find_list = pattern.findall(text)  # 列表形式存储的结果
    return (find_list)


# ================偷揉图床或贴吧图片抽取地址================
def ClipPic():
    read_text = ReadClip()
    info_line = []
    if "sinaimg.cn/large/" in read_text:  # 偷揉图床
        # ================正则匹配================
        re_pattern = r'http://ww[0-9].sinaimg.cn/large/[^)"]*'
        # 匹配http://ww2.sinaimg.cn/large/a15b4afegw1f52rdah5gfj21hk1564hc
        # ================使用Pattern匹配文本，获得全部匹配结果================
        find = ReFind(read_text, re_pattern)  # 列表形式存储的结果
        check_set = set()  # 初始化为空集合
        for i in range(len(find)):
            full_html = '<img src="' + find[i] + '" />'
            if full_html in check_set:
                pass
            else:
                check_set.add(full_html)
                info_line.append(full_html)
    elif "http://imgsrc.baidu.com/forum/pic/item/" in read_text:  # 贴吧图片
        # ================正则匹配================
        re_pattern = r'http://imgsrc.baidu.com/forum/pic/item/[^)]*'
        # ================使用Pattern匹配文本，获得全部匹配结果================
        find = ReFind(read_text, re_pattern)  # 列表形式存储的结果
        for i in range(len(find)):
            info_line.append(find[i])
    info = "\r\n".join(info_line)
    print(info)
    print(len(info_line))
    WriteClip(info)


# ================处理未声明编码的网页================
def GetPage(url):
    import requests
    # url = "http://bbs.jjwxc.net/showmsg.php?board=3&boardpagemsg=1&id=876571"
    page = requests.get(url)

    html = page.content.decode("gb2312", "ignore")
    return html


# ================对字符串算MD5================
def HashMD5String(string):
    import hashlib
    hash_object = hashlib.md5(string.encode('utf-8'))
    return hash_object.hexdigest()


# ================对文件算MD5================
def HashMD5File(path):
    import hashlib, os, time
    start_time = time.time()  # 初始时间戳

    # if os.path.isfile(path) and os.path.exists(path):  # 判断目标是否文件,及是否存在
    hash_object = hashlib.md5(open(path, 'rb').read())

    print(RunTime(start_time))
    return hash_object.hexdigest()


# ================对文件算MD5================
def md5sum(filename, blocksize=65536):
    import hashlib, time
    start_time = time.time()  # 初始时间戳

    hash = hashlib.md5()
    with open(filename, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hash.update(block)
    print(RunTime(start_time))

    return hash.hexdigest()


# ================计算MD5================
def HashMD5(what):
    import hashlib, os
    if os.path.isfile(what):  # 判断目标是否文件
        path = what
        hash_object = hashlib.md5(open(path, 'rb').read())
    elif isinstance(what, str):
        string = what
        hash_object = hashlib.md5(string.encode('utf-8'))
    return hash_object.hexdigest()


# ================用Xpath选取网页元素================
def Xpath(url, xpath):
    from lxml import html
    import requests
    page = requests.get(url)
    tree = html.fromstring(page.text)
    list = tree.xpath(xpath)
    return list


# ================将中文转为编码================
def UEncode(string):
    encoded = string.encode("unicode-escape").decode("utf-8")
    return encoded


# ================CSV格式规范================
def csvconvert(string):
    converted_string = string.replace('"', '""')
    return converted_string


def ReadChrome(input_file_path):
    import time, re, MyDef
    from lxml import html

    start_time = time.time()  # 初始时间戳

    # ==============读取文本==============
    input_file_path = '/Users/alicewish/Dropbox/百度云 网盘-我的分享.htm'
    read_text = open(input_file_path, 'r').read()  # 读取文本
    tree = html.fromstring(read_text)

    # ==============读取文件名==============
    names = tree.xpath('//span[@node-type="name-text"]/@title')  # 列表存储
    all_name = '\r\n'.join(names)
    print(len(names))
    print(all_name)

    # ==============读取下载地址==============
    share_links = []
    links = tree.xpath('//a[@target="_blank"]/@href')  # 列表存储
    for link in links:
        # print(link)
        if re.match(r'https://pan.baidu.com/s/[^<]*', link):  # 判断是否度盘外链
            share_links.append(link)
    all_link = '\n'.join(share_links)
    print(len(share_links))
    print(all_link)

    # ==============读取分享时间和浏览、保存、下载次数==============
    raw_share_time = tree.xpath('//div[@style="width: 20%"]/text()')  # 列表存储分享时间
    all_number = tree.xpath('//div[@style="width: 9%"]/text()')  # 列表存储各类次数

    share_time = []
    view_number = []
    save_number = []
    download_number = []

    for i in range(len(names)):
        share_time.append(raw_share_time[i + 1].strip(" \n\t\r"))
        view_number.append(all_number[3 * i + 3].strip(" \n\t\r").strip("次"))  # 浏览次数
        save_number.append(all_number[3 * i + 4].strip(" \n\t\r").strip("次"))  # 保存次数
        download_number.append(all_number[3 * i + 5].strip(" \n\t\r").strip("次"))  # 下载次数

    # ==============合并信息==============
    info_list = []
    refer_dict = {}
    if len(names) == len(share_links):
        for i in range(len(names)):
            info_line_in_list = [names[i], share_links[i], share_time[i], view_number[i], save_number[i],
                                 download_number[i]]
            info_line = "\t".join(info_line_in_list)
            info_list.append(info_line)
            if len(names[i]) == 64:
                real_name = MyDef.HexShiftBack(names[i][:32])  # 重要
                refer_dict[real_name] = share_links[i]
    else:
        print("错误", len(names), len(share_links))
    all_info = '\n'.join(info_list)

    print(all_info)
    print(MyDef.RunTime(start_time))
    return refer_dict

def HexShift(string):
    shifted_string = string.translate(str.maketrans("0123456789abcdef", "ghijklmnopqrstuv"))
    return shifted_string

def HexShiftBack(string):
    shifted_string = string.translate(str.maketrans("ghijklmnopqrstuv", "0123456789abcdef"))
    return shifted_string

# print(HashMD5('whatever your string is'))

# path = '/Volumes/Mack/~Week 0-Day/0-Day Week of 2016.09.21/Batman 007 (2016) (2 covers) (Digital) (Zone-Empire).cbr'
#
# print(HashMD5(path))
# print(HashMD5(path))
# print(md5sum(path))

# ID = "1788862154"
# print(Xpath('http://sinacn.weibodangan.com//user/' + ID, '//h3[@class="username"]/text()'))
# print(UEncode("中文"))
# print(GetFolderSize('/Volumes/Mack/汉化/'))

# print(ReadCSV("/Users/alicewish/Dropbox/0 Day Week文件地址-墨问非名制作-20160926(15025).csv")[10001][0])

# ================CSV格式规范================


# print(HexShiftBack(HexShift("ff93f17de517de016beffb01f0661db5")))

input_file_path='/Users/alicewish/Downloads/百度云 网盘-Alex_____thor的分享.htm'
# ReadChrome(input_file_path)