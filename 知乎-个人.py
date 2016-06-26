from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================

from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')
me = client.me()
print('用户名', me.name)
print('签名', me.headline)
print('个人描述', me.description)

print('关注话题个数', me.following_topic_count)
print('关注人数', me.following_count)
print('粉丝数', me.follower_count)

print('赞同数', me.voteup_count)
print('感谢数', me.thanked_count)

print('回答数', me.answer_count)
print('提问数', me.question_count)
print('收藏栏数', me.collection_count)
print('文章数', me.articles_count)
print('关注专栏数', me.following_column_count)
print('友善度', me.friendly_score)
print(me.sina_weibo_name)

gayscript = client.people("gayscript")
print('用户名', gayscript.name)
print('签名', gayscript.headline)
print('个人描述', gayscript.description)

print('关注话题个数', gayscript.following_topic_count)
print('关注人数', gayscript.following_count)
print('粉丝数', gayscript.follower_count)

print('赞同数', gayscript.voteup_count)
print('感谢数', gayscript.thanked_count)

print('回答数', gayscript.answer_count)
print('提问数', gayscript.question_count)
print('收藏栏数', gayscript.collection_count)
print('文章数', gayscript.articles_count)
print('关注专栏数', gayscript.following_column_count)
print('友善度', gayscript.friendly_score)
print('关联微博', gayscript.sina_weibo_name)
# ========================查询========================

guchedan = client.people("gu-che-dan")

print('用户名', guchedan.name)
print('签名', guchedan.headline)
print('个人描述', guchedan.description)
print('关注话题个数', guchedan.following_topic_count)
print('关注人数', guchedan.following_count)
print('粉丝数', guchedan.follower_count)
print('赞同数', guchedan.voteup_count)
print('感谢数', guchedan.thanked_count)
print('回答数', guchedan.answer_count)
print('提问数', guchedan.question_count)
print('收藏栏数', guchedan.collection_count)
print('文章数', guchedan.articles_count)
print('关注专栏数', guchedan.following_column_count)
print('友善度', guchedan.friendly_score)
print('关联微博', guchedan.sina_weibo_name)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
