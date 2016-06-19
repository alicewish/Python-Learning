import requests, time
from lxml import html

start_time = time.time()

chapterID = '10469'
page = requests.get('http://www.8kana.com/read/' + chapterID + '.html')
tree = html.fromstring(page.text)
paragraph_list = tree.xpath('//p[@id>0]/text()')
title = tree.xpath('//h2[@class="readbook_title"]/text()')[0]
text = ''.join(paragraph_list)

print(title)
print(text)

# 计时模块
run_time = time.time() - start_time
if run_time < 60:
    print("耗时: {:.2f}秒".format(run_time))
elif run_time < 3600:
    print("耗时: {:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:
    print("耗时: {:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
