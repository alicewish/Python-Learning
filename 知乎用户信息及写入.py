import requests, time, json

start_time = time.time()

user_name = 'Ednak'
html = requests.get('http://api.kanzhihu.com/searchuser/' + user_name)

data = json.loads(html.text)  # 将json字符串转换成python对象
users = data['users']
first_user = users[0]
user_hash = first_user['hash']

html = requests.get('http://api.kanzhihu.com/userdetail2/' + user_hash)
data = json.loads(html.text)  # 将json字符串转换成python对象

detail = data['detail']
star = data['star']

followee = detail['followee']
mostvote10 = detail['mostvote10']
answer = detail['answer']
fratio = detail['fratio']
agreeiw = detail['agreeiw']
agreeiratio = detail['agreeiratio']
agreei = detail['agreei']
ask = detail['ask']
followeri = detail['followeri']
fav = detail['fav']
mostvotepercent = detail['mostvotepercent']
count5000 = detail['count5000']
mostvote5 = detail['mostvote5']
count100 = detail['count100']
post = detail['post']
mostvote5percent = detail['mostvote5percent']
mostvote = detail['mostvote']
followiratiow = detail['followiratiow']
count2000 = detail['count2000']
count10000 = detail['count10000']
ratio = detail['ratio']
followiratio = detail['followiratio']
thanks = detail['thanks']
tratio = detail['tratio']
agree = detail['agree']
count200 = detail['count200']
followeriw = detail['followeriw']
follower = detail['follower']
agreeiratiow = detail['agreeiratiow']
logs = detail['logs']
mostvote10percent = detail['mostvote10percent']
count1000 = detail['count1000']
count500 = detail['count500']

count100rank = star['count100rank']
ratiorank = star['ratiorank']
favrank = star['favrank']
answerrank = star['answerrank']
agreerank = star['agreerank']
count1000rank = star['count1000rank']
followerrank = star['followerrank']

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
info = (now, '知乎昵称 ' + user_name, '回答数 ' + answer, '专栏文章数 ' + post, '赞同数 ' + agree, '1日赞同数增加 ' + agreei,
        '1日赞同数增幅 ' + agreeiratio, '7日赞同数增加 ' + agreeiw, '7日赞同数增幅 ' + agreeiratiow, '被关注数（粉丝） ' + follower,
        '1日被关注数增加 ' + followeri, '1日被关注数增幅 ' + followiratio, '7日被关注数增加 ' + followeriw, '7日被关注数增幅 ' + followiratiow,
        '感谢数 ' + thanks, '收藏数 ' + fav, '最高赞同 ' + mostvote, '最高赞同占比 ' + mostvotepercent, '前5赞同 ' + mostvote5,
        '前5赞同占比 ' + mostvote5percent, '最高赞同 ' + mostvote, '最高赞同占比 ' + mostvotepercent, '前10赞同 ' + mostvote10,
        '前10赞同占比 ' + mostvote10percent, '回答数+专栏文章数排名 ' + answerrank, '赞同数排名 ' + agreerank, '平均赞同排名 ' + ratiorank,
        '被关注数排名 ' + followerrank, '收藏数排名 ' + favrank, '', '')
text = '\r\n'.join(info)
print(text)
f = open('/Users/alicewish/我的坚果云/知乎.txt', 'a')
try:
    f.write(text)
finally:
    f.close()
# 计时模块
run_time = time.time() - start_time
if run_time < 60:
    print("耗时: {:.2f}秒".format(run_time))
elif run_time < 3600:
    print("耗时: {:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:
    print("耗时: {:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
