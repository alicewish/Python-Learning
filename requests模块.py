import requests, time

start_time = time.time()  # 初始时间戳

page = requests.get("http://xlzd.me/query", params={"name": "xlzd", "lang": "python"})
print(page.url)
page = requests.get('http://xlzd.me')
print(page.encoding)
print(page.headers)
print(page.cookies)
print(page.text)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
