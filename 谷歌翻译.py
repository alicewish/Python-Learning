from lxml import html
import requests, time


start_time = time.time()

# -*- coding: utf-8 -*-
import httplib
from urllib import urlencode
import re
def out(text):
    p = re.compile(r'","')
    m = p.split(text)
    print m[0][4:].decode('UTF-8').encode('GBK')
if __name__=='__main__':
    while True:
        word=raw_input('Input the word you want to search:')
        text=urlencode({'text':word})
        h=httplib.HTTP('translate.google.cn')
        h.putrequest('GET', '/translate_a/t?client=t&hl=zh-CN&sl=en&tl=zh-CN&ie=UTF-8&oe=UTF-8&'+text)
        h.endheaders()
        h.getreply()
        f = h.getfile()
        lines = f.readlines()
        out(lines[0])
        f.close()

# 计时模块
run_time = time.time() - start_time
if run_time < 60:
    print("耗时: {:.2f}秒".format(run_time))
elif run_time < 3600:
    print("耗时: {:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:
    print("耗时: {:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
