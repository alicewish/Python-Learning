import requests, time, json

start_time = time.time()  # 初始时间戳

user_name='墨问非名'
html = requests.get('http://api.kanzhihu.com/searchuser/'+user_name)

data = json.loads(html.text)  # 将json字符串转换成python对象
users = data['users']
first_user=users[0]
user_hash=first_user['hash']

print(user_hash)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
