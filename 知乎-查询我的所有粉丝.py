from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ========================我========================
me = client.me()
# ==================查询我的粉丝==================
followers_line = []
for follower in me.followers:
    # 查询所有可用信息
    activities = follower.activities
    answer_count = follower.answer_count
    answers = follower.answers
    articles = follower.articles
    articles_count = follower.articles_count
    avatar_url = follower.avatar_url
    business = follower.business
    collected_count = follower.collected_count
    collection_count = follower.collection_count
    collections = follower.collections
    column_count = follower.column_count
    columns = follower.columns
    columns_count = follower.columns_count
    created_at = follower.created_at
    description = ((follower.description).replace("\t","")).replace("\n","|") #清理会打乱数据的换行和制表符
    draft_count = follower.draft_count
    educations = follower.educations
    email = follower.email
    employments = follower.employments
    favorite_count = follower.favorite_count
    favorited_count = follower.favorited_count
    follower_count = follower.follower_count
    followers = follower.followers
    following_column_count = follower.following_column_count
    following_columns = follower.following_columns
    following_count = follower.following_count
    following_question_count = follower.following_question_count
    following_questions = follower.following_questions
    following_topic_count = follower.following_topic_count
    following_topics = follower.following_topics
    followings = follower.followings
    friendly_score = follower.friendly_score
    gender = follower.gender
    has_daily_recommend_permission = follower.has_daily_recommend_permission
    headline = ((follower.headline).replace("\t","")).replace("\n","|") # 清理会打乱数据的换行和制表符
    id = follower.id
    is_active = follower.is_active
    is_baned = follower.is_baned
    is_bind_sina = follower.is_bind_sina
    is_locked = follower.is_locked
    is_moments_user = follower.is_moments_user
    locations = follower.locations
    name = follower.name
    question_count = follower.question_count
    questions = follower.questions
    shared_count = follower.shared_count
    sina_weibo_name = follower.sina_weibo_name
    sina_weibo_url = follower.sina_weibo_url
    thanked_count = follower.thanked_count
    uid = follower.uid
    voteup_count = follower.voteup_count
    # 整理
    follower_info = [name, str(gender), str(voteup_count), str(follower_count), str(answer_count), str(articles_count),str(description), str(headline), str(email), str(sina_weibo_name), str(sina_weibo_url)]
    info_line = '\t'.join(follower_info)
    print(info_line)
    followers_line.append(info_line)
# 合并数据
text = '\r\n'.join(followers_line)

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
