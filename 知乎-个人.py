from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================

from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ========================我========================
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
print('关联微博', me.sina_weibo_name)

# ========================查询粉丝========================
for follower in me.followers:
    print(follower.name, follower.sina_weibo_name, follower.follower_count)

# # ========================查询他人========================
# people = client.people("gu-che-dan")
#
# print('用户名', people.name)
# print('签名', people.headline)
# print('个人描述', people.description)
# print('关注话题个数', people.following_topic_count)
# print('关注人数', people.following_count)
# print('粉丝数', people.follower_count)
# print('赞同数', people.voteup_count)
# print('感谢数', people.thanked_count)
# print('回答数', people.answer_count)
# print('提问数', people.question_count)
# print('收藏栏数', people.collection_count)
# print('文章数', people.articles_count)
# print('关注专栏数', people.following_column_count)
# print('友善度', people.friendly_score)
# print('关联微博', people.sina_weibo_name)
# # ========================查询问题========================
# question = client.question(22384666)
# print('答案数', question.answer_count)
# print('关注数', question.follower_count)

# # ========================查询话题========================
# topic = client.topic(19668865)
# print('图标地址', topic.avatar_url)
# print('最佳回答数', topic.best_answer_count)
# print('最佳回答者详情', topic.best_answerers)
# print('精华回答', topic.best_answers)
# print('精华回答数', topic.best_answers_count)
# print('子话题', topic.children)
# print('摘录', topic.excerpt)
# print('父数', topic.father_count)
# print('关注？', topic.follower_count)
# print('关注', topic.followers)
# print('关注人数', topic.followers_count)
# print('话题ID', topic.id)
# print('介绍', topic.introduction)
# print('名称', topic.name)
# print('父话题数', topic.parent_count)
# print('父话题详情', topic.parents)
# print('已回答问题数', topic.question_count)
# print('已回答问题个数', topic.questions_count)
# print('未回答问题数', topic.unanswered_count)
# print('未回答问题', topic.unanswered_questions)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
