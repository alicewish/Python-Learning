# ========================函数区开始========================

def RandomSample(MD5_list, number=10):
    import random
    if number < len(MD5_list):
        random_sample = random.sample(MD5_list, number)
    else:
        random_sample = MD5_list
    print(random_sample)
    random_sample.sort()
    remain_sample = list(set(MD5_list).difference(set(random_sample)))
    return (random_sample, remain_sample)


def ReadMD5CSV():
    import os, MyDef
    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)  # 词典文件的地址
    MD5_refer_dict = MyDef.ReadDictC(refer_file_path, True)

    MD5_list = []
    for file_MD5 in MD5_refer_dict:
        MD5_list.append(file_MD5)
    return (MD5_refer_dict, MD5_list)


# ========================输入区开始========================

def Sampling(number=30):
    import time, MyDef, os

    start_time = time.time()  # 初始时间戳

    MD5_refer_dict, MD5_list = ReadMD5CSV()

    remain_sample = MD5_list
    refer_dict = {}
    while len(remain_sample) > 0:
        random_sample, remain_sample = RandomSample(remain_sample, number)
        random_sample_string = '|'.join(random_sample)
        print(random_sample_string)
        random_sample_string_MD5 = MyDef.HashMD5String(random_sample_string)
        print('方案MD5', random_sample_string_MD5)
        refer_dict[random_sample_string_MD5] = random_sample_string

    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5随机分样表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)
    MyDef.WriteDictB(refer_dict, refer_file_path)

    print(MyDef.RunTime(start_time))


def ReadMD5SamplingCSV():
    import os, MyDef
    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5随机分样表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)
    return MyDef.ReadDictB(refer_file_path)


def ChangeBack():
    import os, MyDef
    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)
    text_readline = MyDef.ReadCSV(refer_file_path, type=False)
    for i in range(len(text_readline)):
        if '@k_k@' in text_readline[i][1]:
            print(text_readline[i][1])
            text_readline[i][1] = text_readline[i][1].replace('@k_k@', '')
    MyDef.StoreCSV(text_readline, refer_file_path)


def Distribute():
    import time, MyDef, os, shutil
    start_time = time.time()  # 初始时间戳
    refer_dict = ReadMD5SamplingCSV()
    MD5_refer_dict, MD5_list = ReadMD5CSV()

    # ========================最外层目录========================
    new_file_dir = '/Volumes/Mack/Distribute'
    if not os.path.exists(new_file_dir):  # 判断目标是否存在
        try:
            os.mkdir(new_file_dir)  # 创建最外层目录
        except:
            pass
    # ========================主目录========================
    for key in refer_dict:
        folder_name = MyDef.HexShift(key)
        new_folder_path = os.path.join(new_file_dir, folder_name)
        if not os.path.exists(new_folder_path):  # 判断目标是否存在
            try:
                os.mkdir(new_folder_path)  # 创建目录
            except:
                pass
        sample_list = refer_dict[key].split("|")
        print(sample_list)
        # ========================次级目录========================
        for sample in sample_list:  # 文件MD5
            file_path = MD5_refer_dict[sample]
            file_name = os.path.split(file_path)[1]
            print("旧", file_path)
            file_folder_name = MyDef.HexShift(sample)

            new_file_folder_path = os.path.join(new_file_dir, folder_name, folder_name + file_folder_name)

            try:
                os.mkdir(new_file_folder_path)  # 创建目录
            except:
                pass

            new_file_path = os.path.join(new_file_folder_path, file_name)
            print("新", new_file_path)

            try:
                shutil.move(file_path, new_file_path)  # 移动文件或目录都是使用这条命令
            except:
                pass

    print(MyDef.RunTime(start_time))


def UnDistribute():
    import time, MyDef, os, shutil
    start_time = time.time()  # 初始时间戳
    refer_dict = ReadMD5SamplingCSV()
    MD5_refer_dict, MD5_list = ReadMD5CSV()
    new_file_dir = '/Volumes/Mack/Distribute'

    for key in refer_dict:
        new_folder_path = os.path.join(new_file_dir, key)

        sample_list = refer_dict[key].split("|")
        print(sample_list)
        for sample in sample_list:
            file_path = MD5_refer_dict[sample]
            file_name = os.path.split(file_path)[1]
            print("旧", file_path)
            new_file_path = os.path.join(new_folder_path, sample, file_name)
            print("新", new_file_path)

            try:
                shutil.move(new_file_path, file_path)  # 移动文件或目录都是使用这条命令
            except:
                pass

    print(MyDef.RunTime(start_time))


def ReadOpera():
    import time, re, MyDef
    from lxml import html

    start_time = time.time()  # 初始时间戳

    # ==============读取文本==============
    input_file_path = '/Users/alicewish/Dropbox/百度云 网盘-我的分享.html'
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


def BulidLinkA():
    import time, MyDef, os
    start_time = time.time()  # 初始时间戳
    refer_dict = ReadMD5SamplingCSV()
    MD5_refer_dict, MD5_list = ReadMD5CSV()
    yun_link_dict = ReadOpera()
    output_list = []
    # ========================主目录========================
    for key in refer_dict:
        if key in yun_link_dict:
            folder_name = MyDef.HexShift(key)
            yun_link = yun_link_dict[key]

            sample_list = refer_dict[key].split("|")
            print(sample_list)
            # ========================次级目录========================
            for sample in sample_list:  # 文件MD5
                file_path = MD5_refer_dict[sample]
                file_name = os.path.split(file_path)[1]

                file_folder_name = MyDef.HexShift(sample)
                file_link = yun_link + '#path=%252F' + folder_name + '%252F' + folder_name + file_folder_name
                print(file_name)
                print(file_link)
                path_list = [file_path, file_link]
                output_list.append(path_list)
    path = '/Users/alicewish/Dropbox/漫画图源度盘地址表.csv'
    MyDef.StoreCSV(output_list, path)
    print(len(output_list))
    print(MyDef.RunTime(start_time))




def AddDict(refer_dict):
    import requests, MyDef
    for k in range(15):

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'}
        url = 'https://pan.baidu.com/wap/share/home?third=0&uk=2007334207&start=' + str(20 * (k + 1))
        page = requests.get(url=url, headers=header)
        # print(page.encoding)
        # print(page.headers)
        # print(page.cookies)
        # print(page.text)
        html = page.content.decode("utf", "ignore")
        # print(html)


        shareid_list = MyDef.ReFind(html, r'"shareid":"[0-9]{1,20}')

        print(shareid_list)
        print(len(shareid_list))

        title_list = MyDef.ReFind(html, r'"title":"[a-z]{64}')
        print(title_list)
        print(len(title_list))

        for i in range(len(shareid_list)):
            shareid = shareid_list[i].replace('"shareid":"', '')
            title = title_list[i].replace('"title":"', '')
            real_name = MyDef.HexShiftBack(title[:32])
            refer_dict[real_name] = 'https://pan.baidu.com/share/link?uk=2007334207&shareid=' + shareid
    return refer_dict


def ReadMobile():
    import time, requests, MyDef

    start_time = time.time()  # 初始时间戳
    refer_dict = {}

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'}
    url = 'https://pan.baidu.com/wap/share/home?uk=2007334207&third=0'
    page = requests.get(url=url, headers=header)
    # print(page.encoding)
    # print(page.headers)
    # print(page.cookies)
    # print(page.text)
    html = page.content.decode("utf", "ignore")
    # print(html)


    shareid_list = MyDef.ReFind(html, r'"shareid":"[0-9]{1,20}')

    print(shareid_list)
    print(len(shareid_list))

    title_list = MyDef.ReFind(html, r'"title":"[a-z]{64}')
    print(title_list)
    print(len(title_list))

    for i in range(len(shareid_list)):
        shareid = shareid_list[i].replace('"shareid":"', '')
        title = title_list[i].replace('"title":"', '')
        real_name = MyDef.HexShiftBack(title[:32])
        refer_dict[real_name] = 'https://pan.baidu.com/share/link?uk=2007334207&shareid=' + shareid

    refer_dict = AddDict(refer_dict)

    # ================运行时间计时================
    print(MyDef.RunTime(start_time))
    print(refer_dict)
    print(len(refer_dict))
    return refer_dict


def BulidLinkB():
    import time, MyDef, os
    start_time = time.time()  # 初始时间戳
    refer_dict = ReadMD5SamplingCSV()
    MD5_refer_dict, MD5_list = ReadMD5CSV()
    yun_link_dict = ReadMobile()
    output_list = []
    # ========================主目录========================
    for key in refer_dict:
        if key in yun_link_dict:
            folder_name = MyDef.HexShift(key)
            yun_link = yun_link_dict[key]

            sample_list = refer_dict[key].split("|")
            print(sample_list)
            # ========================次级目录========================
            for sample in sample_list:  # 文件MD5
                file_path = MD5_refer_dict[sample]
                file_name = os.path.split(file_path)[1]

                file_folder_name = MyDef.HexShift(sample)
                file_link = yun_link + '#path=%252F' + folder_name + '%252F' + folder_name + file_folder_name
                print(file_name)
                print(file_link)
                path_list = [file_path, file_link]
                output_list.append(path_list)
    path = '/Users/alicewish/Dropbox/漫画图源度盘地址表.csv'
    MyDef.StoreCSV(output_list, path)
    print(len(output_list))
    print(MyDef.RunTime(start_time))

BulidLinkB()