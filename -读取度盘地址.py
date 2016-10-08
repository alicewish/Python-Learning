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
            refer_dict[title] = 'https://pan.baidu.com/share/link?uk=2007334207&shareid=' + shareid
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
        refer_dict[title] = 'https://pan.baidu.com/share/link?uk=2007334207&shareid=' + shareid

    refer_dict = AddDict(refer_dict)

    # ================运行时间计时================
    print(MyDef.RunTime(start_time))
    print(refer_dict)
    print(len(refer_dict))
    return refer_dict


# ReadMobile()



