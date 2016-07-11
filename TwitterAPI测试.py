from lxml import html
import requests, time, twitter

start_time = time.time()  # 初始时间戳
api = twitter.Api(consumer_key=["RrajNOp4TQetAuMLEG1BGGQmC"],
                  consumer_secret=["jqumaSJHcQOPdhVblHi6chb9CawYpYJlcIR3ny8rgHjUFVvnDU"],
                  access_token_key=["176644256-y3dOu0IPhvxGY6iIoqtqTYMx2VQiX05FVEUq4Jgr"],
                  access_token_secret=["tgKaiH0S02cR6DkrkTgcAPa4N0WurNy1bK8d1WYI0Ti57"])

users = api.GetFriends()
for u in users:
    print(u.screen_name)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
