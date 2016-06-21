# -*- coding:utf-8 -*-
import urllib2
import urllib
import cookielib
import re
import requests
import xlwt

import lxml.html as HTML


def set_style(name, height, bold=False, center=True):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = False
    font.color_index = 0
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    if center == True:
        style.alignment = alignment
    return style


cook = {
    "cookie": " _T_WM=f7f85a843a00d6cb75127f6738048684; SUB=_2A2570rYGDeTxGeVH6lMY8CrNyTSIHXVZPNpOrDV6PUNbvtBeLXjCkW1LHes9Ieus0jFlbqH-zK9mrfPf5RIYUA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFP5ViyVnhP5v7lWsyRUFBe5JpX5KMt; SUHB=0tK68KutxlwRZo; SSOLoginState=1456916054; gsid_CTandWM=4ujnCpOz5UnDiYJOrOlsZgpFe24"}

num = 0

arr = []

f = file("C:/cache/users.txt", "w")

for x in range(1, 25, 1):
    tmp = '%d' % x
    url = 'http://weibo.cn/3911904128/follow?page=' + tmp
    print
    url
    html = requests.get(url, cookies=cook).content

    regex1 = re.compile(r'top"><a.*?href="http://weibo.cn/u/(.*?)"\>.*?<\/a>');
    # get the ids of the users

    urls = re.findall(regex1, html)
    for i in urls:
        flag = 1
        for j in range(0, num, 1):
            if arr[j] == i:
                flag = 0
        if flag == 1:
            arr.append(i)
            num = num + 1
            print
            i
            f.write(i)
            f.write('\n')

print
num

f.close()
# 以上代码获取了103个用户的信息(uid)

f = file("C:/cache/info.txt", "w")
fx = xlwt.Workbook(encoding='utf-8')
sheet1 = fx.add_sheet(u'sheet1', cell_overwrite_ok=True)
sheet1.col(0).width = 2000
for i in range(1, 14, 1):
    sheet1.col(i).width = 5000
sheet1.col(4).width = 2000
sheet1.col(6).width = 8000
sheet1.col(7).width = 8000
sheet1.col(8).width = 8000
sheet1.write_merge(0, 0, 1, 9, u'基本信息', set_style('Times New Roman', 220, True, True))
sheet1.write_merge(0, 0, 10, 12, u'工作信息', set_style('Times New Roman', 220, True, True))
sheet1.write(0, 13, u'教育信息', set_style('Times New Roman', 220, True, True))

row = [u'No.', u'用户id', u'昵称', u'所在地', u'性别', u'生日', u'博客', u'个性域名', u'简介', u'注册时间', u'公司', u'地区', u'职位', u'教育信息']

for i in range(0, 14, 1):
    sheet1.write(1, i, row[i], set_style('Times New Roman', 220, True, False))

cook = {
    'cookie': 'SINAGLOBAL=2182977036572.993.1445214114592; myuid=3911904128; un=397158185@qq.com; wvr=6; UOR=blog.ifeng.com,widget.weibo.com,cuiqingcai.com; SUS=SID-3911904128-1456916053-GZ-gunir-8b376c752210cba73a1347f8b0f5aa2f; SUE=es%3Dda1008350893b250a3a74e93ba53a806%26ev%3Dv1%26es2%3D378a57c494c69e06a11515fc522e8f03%26rs0%3D7XQ3u3DY0jjwq5KRgVbZ0x%252BT73dtJ1NoLTOA5LEB3VBSmjfVM6ZcamVNtc7%252Fi2dkDzHTp%252F9tILk%252F9AaPb0RBMfhOE1SAWbVuMkEgcrmMCmwsQr7CiTP7pZhwfMMrIm8x%252BxXBVJVLmyS20Elh9okKXd9h7iDhYWM3Bctn2kY0Hww%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1456916053%26et%3D1457002453%26d%3Dc909%26i%3Daa2f%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D3911904128%26name%3D397158185%2540qq.com%26nick%3D%25E5%25B0%258F%25E5%258F%25A4_akari%26fmp%3D%26lcp%3D; SUB=_2A2570rYFDeTxGeVH6lMY8CrNyTSIHXVYqaDNrDV8PUNbvtBeLXWmkW9LHettJ2LhIMROoKHoomaRtTwBu0fdzA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFP5ViyVnhP5v7lWsyRUFBe5JpX5KMt; SUHB=0XD1tT359tP9n1; ALF=1488452052; SSOLoginState=1456916053; _s_tentry=-; Apache=8211320573464.036.1456916151430; ULV=1456916151458:55:3:4:8211320573464.036.1456916151430:1456876755770'}
for i in range(0, 100, 1):
    i0 = i + 1
    tmp = '%d' % i0
    f.write('No.' + tmp + ':\n')
    url = 'http://weibo.com/' + arr[i] + '/info'
    # url = 'http://weibo.com/1402400261/info'
    print
    url
    html = requests.get(url, cookies=cook).content
    f.write(url + '\n\n')
    # f.write(html+'\n\n')
    f.write('用户id： ' + arr[i] + '\n')
    sheet1.write(i + 2, 0, tmp, set_style('Times New Roman', 220, True, False))
    sheet1.write(i + 2, 1, arr[i], set_style('Times New Roman', 220, True, False))
    f.write('基本信息：\n')

    regex2 = re.compile(r'昵称：<\\/span><span class=\\"pt_detail\\">(.*?)<\\/span>');
    t = re.findall(regex2, html)
    if t:
        f.write('  昵称： ')
        for s in t:
            f.write(s + '\n')
            sheet1.write(i + 2, 2, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(r'所在地：<\\/span><span class=\\"pt_detail\\">(.*?)<\\/span>');
    t = re.findall(regex2, html)
    if t:
        f.write('  所在地： ')
        for s in t:
            f.write(s + '\n')
            sheet1.write(i + 2, 3, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(r'性别：<\\/span><span class=\\"pt_detail\\">(.*?)<\\/span>');
    t = re.findall(regex2, html)
    if t:
        f.write('  性别： ')
        for s in t:
            f.write(s + '\n')
            sheet1.write(i + 2, 4, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(r'生日：<\\/span><span class=\\"pt_detail\\">(.*?)<\\/span>');
    t = re.findall(regex2, html)
    if t:
        f.write('  生日： ')
        for s in t:
            f.write(s + '\n')
            sheet1.write(i + 2, 5, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(r'博客：<\\/span>\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t<a href=\\"(.*?)\?from=');
    t = re.findall(regex2, html)
    if t:
        f.write('  博客： ')
        for s in t:
            s = s.replace('\\', '')
            f.write(s + '\n')
            sheet1.write(i + 2, 6, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(
        r'个性域名：<\\/span>\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t<span class=\\"pt_detail\\">\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t<a href=\\"(.*?)\?from=');
    t = re.findall(regex2, html)
    if t:
        f.write('  个性域名： ')
        for s in t:
            s = s.replace('\\', '')
            f.write(s + '\n')
            sheet1.write(i + 2, 7, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(
        r'简介：<\\/span>\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t<span class=\\"pt_detail\\">(.*?)<\\/span>');
    t = re.findall(regex2, html)
    if t:
        f.write('  简介： ')
        for s in t:
            f.write(s + '\n')
            sheet1.write(i + 2, 8, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(
        r'注册时间：<\\/span>\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t<span class=\\"pt_detail\\">\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t(.*?)\\t');
    t = re.findall(regex2, html)
    if t:
        f.write('  注册时间： ')
        for s in t:
            f.write(s + '\n')
            sheet1.write(i + 2, 9, s, set_style('Times New Roman', 220, True, False))

    f.write('工作信息：\n')

    regex2 = re.compile(r'公司：<.*?blank\\">(.*?)<\\/a>');
    t = re.findall(regex2, html)
    if t:
        f.write('  公司： ')
        for s in t:
            f.write(s)
            s1 = s
        regex3 = re.compile(r'公司：<.*?\\t (\(.*?\))');
        w = re.findall(regex3, html)
        for y in w:
            f.write(y + '\n')
            s = s1 + ' ' + y
            sheet1.write(i + 2, 10, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(r'地区：(.*?)<br');
    t = re.findall(regex2, html)
    if t:
        f.write('  地区： ')
        for s in t:
            f.write(s + '\n')
            sheet1.write(i + 2, 11, s, set_style('Times New Roman', 220, True, False))

    regex2 = re.compile(r'职位：(.*?)\\t');
    t = re.findall(regex2, html)
    if t:
        f.write('  职位： ')
        for s in t:
            f.write(s + '\n')
            sheet1.write(i + 2, 12, s, set_style('Times New Roman', 220, True, False))

    f.write('教育信息：\n')

    s1 = ''
    s2 = ''
    s3 = ''
    regex2 = re.compile(r'教育信息<\\/.*?2\\">(.*?)<\\/span>');
    t = re.findall(regex2, html)
    if t:
        for s in t:
            f.write('  ' + s + ' ')
            s1 = s

    regex2 = re.compile(r'教育信息.*?infedu\\">(.*?)<\\/a>');
    t = re.findall(regex2, html)
    if t:
        for s in t:
            f.write(s + ' ')
            s2 = s

    regex2 = re.compile(r'教育信息.*?a> (\(.*?\))');
    t = re.findall(regex2, html)
    if t:
        for s in t:
            f.write(s + '\n')
            s3 = s
    s = s1 + ' ' + s2 + ' ' + s3
    sheet1.write(i + 2, 13, s, set_style('Times New Roman', 220, True, False))
    f.write('\n\n')
fx.save('C:/cache/info.xls')
f.close()
