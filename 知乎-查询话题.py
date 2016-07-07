from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ========================查询话题========================
tid = 19668865
topic = client.topic(tid)
print('图标地址', topic.avatar_url)
print('最佳回答数', topic.best_answer_count)
print('最佳回答者', topic.best_answerers)
print('精华回答', topic.best_answers)
print('精华回答数', topic.best_answers_count)
print('子话题详情', topic.children)
print('摘录', topic.excerpt)
print('父话题数', topic.father_count)
print('关注人数', topic.follower_count)
print('关注人', topic.followers)
print('关注人数', topic.followers_count)
print('话题ID', topic.id)
print('介绍', topic.introduction)
print('名称', topic.name)
print('父话题数', topic.parent_count)
print('父话题详情', topic.parents)
print('已回答问题数', topic.question_count)
print('已回答问题个数', topic.questions_count)
print('未回答问题数', topic.unanswered_count)
print('未回答问题', topic.unanswered_questions)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
