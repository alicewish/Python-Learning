from lxml import html
import requests, time, html2text

start_time = time.time()

html = "<p><strong>Zed's</strong> dead baby, <em>Zed's</em> dead.</p>"
markdown = html2text.html2text(html)
print(markdown)

# 计时模块
run_time = time.time() - start_time
if run_time < 60:
    print("耗时: {:.2f}秒".format(run_time))
elif run_time < 3600:
    print("耗时: {:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:
    print("耗时: {:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
