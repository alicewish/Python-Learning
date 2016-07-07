from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ==================查询话题下所有最佳回答者==================
tid = 19668865
topic = client.topic(tid)
answerers_line = []
for answerer in topic.best_answerers:
    # 查询所有可用信息
    activities = answerer.activities
    answer_count = answerer.answer_count
    answers = answerer.answers
    articles = answerer.articles
    articles_count = answerer.articles_count
    avatar_url = answerer.avatar_url
    business = answerer.business
    collected_count = answerer.collected_count
    collection_count = answerer.collection_count
    collections = answerer.collections
    column_count = answerer.column_count
    columns = answerer.columns
    columns_count = answerer.columns_count
    created_at = answerer.created_at
    description = ((answerer.description).replace("\t", "")).replace("\n", "|")  # 清理会打乱数据的换行和制表符
    draft_count = answerer.draft_count
    educations = answerer.educations
    email = answerer.email
    employments = answerer.employments
    favorite_count = answerer.favorite_count
    favorited_count = answerer.favorited_count
    follower_count = answerer.follower_count
    followers = answerer.followers
    following_column_count = answerer.following_column_count
    following_columns = answerer.following_columns
    following_count = answerer.following_count
    following_question_count = answerer.following_question_count
    following_questions = answerer.following_questions
    following_topic_count = answerer.following_topic_count
    following_topics = answerer.following_topics
    followings = answerer.followings
    friendly_score = answerer.friendly_score
    gender = answerer.gender
    has_daily_recommend_permission = answerer.has_daily_recommend_permission
    headline = answerer.headline
    id = answerer.id
    is_active = answerer.is_active
    is_baned = answerer.is_baned
    is_bind_sina = answerer.is_bind_sina
    is_locked = answerer.is_locked
    is_moments_user = answerer.is_moments_user
    locations = answerer.locations
    name = answerer.name
    question_count = answerer.question_count
    questions = answerer.questions
    shared_count = answerer.shared_count
    sina_weibo_name = answerer.sina_weibo_name
    sina_weibo_url = answerer.sina_weibo_url
    thanked_count = answerer.thanked_count
    uid = answerer.uid
    voteup_count = answerer.voteup_count
    # 整理
    follower_info = [name, str(gender), str(voteup_count), str(follower_count), str(answer_count), str(articles_count),
                     str(description), str(headline), str(email), str(sina_weibo_name), str(sina_weibo_url)]
    info_line = '\t'.join(follower_info)
    print(info_line)
    answerers_line.append(info_line)
# 合并数据
text = '\r\n'.join(answerers_line)

# ================写入剪贴板================
import pyperclip

pyperclip.copy(text)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
