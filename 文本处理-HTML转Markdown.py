from lxml import html
import requests, time, html2text

start_time = time.time()  # 初始时间戳
url="http://bbs.jjwxc.net/showmsg.php?board=3&boardpagemsg=1&id=876571"
html = "<p><strong>Zed's</strong> dead baby, <em>Zed's</em> dead.</p>"
page = requests.get(url)
markdown = html2text.html2text(page.text)
print(markdown)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
