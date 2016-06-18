import requests, time
from lxml import html
#todo
start_time = time.time()

bookID='10077'
page = requests.get('http://www.8kana.com/book/'+bookID+'.html')
tree = html.fromstring(page.text)
chapter_list = tree.xpath('//a[@class="left"][@target="_blank"]/@title')
text='\r\n'.join(chapter_list)

print(text)

# 计时模块
run_time = time.time() - start_time
if run_time < 60:
    print("耗时: {:.2f}秒".format(run_time))
elif run_time < 3600:
    print("耗时: {:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:
    print("耗时: {:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
