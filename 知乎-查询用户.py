from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ============用户模块============
pid = "edna-krabappel"

people = client.people(pid)
print('活动', people.activities)
print('答案数', people.answer_count)
print('答案', people.answers)
print('文章', people.articles)
print('文章数', people.articles_count)
print('头像地址', people.avatar_url)
print('用户所在行业', people.business)
print('收藏数', people.collected_count)
print('收藏夹数', people.collection_count)
print('收藏夹', people.collections)
print('专栏数', people.column_count)
print('专栏', people.columns)
print('专栏数', people.columns_count)
print('创建时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(people.created_at)))
print('个人描述', people.description)
print('草稿数', people.draft_count)
print('教育信息', people.educations)
print('邮箱', people.email)
print('职业信息', people.employments)
print('收藏数', people.favorite_count)
print('被收藏数', people.favorited_count)
print('粉丝数', people.follower_count)
print('粉丝', people.followers)
print('关注数', people.following_column_count)
print('关注专栏', people.following_columns)
print('关注数', people.following_count)
print('关注问题数', people.following_question_count)
print('关注问题', people.following_questions)
print('关注话题数', people.following_topic_count)
print('关注话题', people.following_topics)
print('关注', people.followings)
print('友善度', people.friendly_score)
print('性别', people.gender)
print('有每日推荐权限', people.has_daily_recommend_permission)
print('签名', people.headline)
print('用户ID', people.id)
print('是否活跃', people.is_active)
print('是否被禁', people.is_baned)
print('是否绑定新浪账户', people.is_bind_sina)
print('是否被锁', people.is_locked)
print('是否为Moments用户', people.is_moments_user)
print('位置', people.locations)
print('用户名', people.name)
print('提问数', people.question_count)
print('提问', people.questions)
print('分享数', people.shared_count)
print('微博昵称', people.sina_weibo_name)
print('微博地址', people.sina_weibo_url)
print('感谢数', people.thanked_count)
print('用户UID', people.uid)
print('赞同数', people.voteup_count)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
