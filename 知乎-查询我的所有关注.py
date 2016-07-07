import time

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ========================我========================
me = client.me()
# ==================查询我的关注==================
followings_line = []
for following in me.followings:
    # 查询所有可用信息
    activities = following.activities
    answer_count = following.answer_count
    answers = following.answers
    articles = following.articles
    articles_count = following.articles_count
    avatar_url = following.avatar_url
    business = following.business
    collected_count = following.collected_count
    collection_count = following.collection_count
    collections = following.collections
    column_count = following.column_count
    columns = following.columns
    columns_count = following.columns_count
    created_at = following.created_at
    description = ((following.description).replace("\t", "")).replace("\n", "|")  # 清理会打乱数据的换行和制表符
    draft_count = following.draft_count
    educations = following.educations
    email = following.email
    employments = following.employments
    favorite_count = following.favorite_count
    favorited_count = following.favorited_count
    following_count = following.following_count
    followings = following.followings
    following_column_count = following.following_column_count
    following_columns = following.following_columns
    following_count = following.following_count
    following_question_count = following.following_question_count
    following_questions = following.following_questions
    following_topic_count = following.following_topic_count
    following_topics = following.following_topics
    followings = following.followings
    friendly_score = following.friendly_score
    gender = following.gender
    has_daily_recommend_permission = following.has_daily_recommend_permission
    headline = ((following.headline).replace("\t", "")).replace("\n", "|")  # 清理会打乱数据的换行和制表符
    id = following.id
    is_active = following.is_active
    is_baned = following.is_baned
    is_bind_sina = following.is_bind_sina
    is_locked = following.is_locked
    is_moments_user = following.is_moments_user
    locations = following.locations
    name = following.name
    question_count = following.question_count
    questions = following.questions
    shared_count = following.shared_count
    sina_weibo_name = following.sina_weibo_name
    sina_weibo_url = following.sina_weibo_url
    thanked_count = following.thanked_count
    uid = following.uid
    voteup_count = following.voteup_count
    # 整理
    following_info = [name, str(gender), str(voteup_count), str(following_count), str(answer_count),
                      str(articles_count), str(description), str(headline), str(sina_weibo_name), str(sina_weibo_url)]
    info_line = '\t'.join(following_info)
    print(info_line)
    followings_line.append(info_line)
# 合并数据
text = '\r\n'.join(followings_line)

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
