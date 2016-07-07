from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ========================我========================
me = client.me()
print('活动', me.activities)
print('答案数', me.answer_count)
print('答案', me.answers)
print('文章', me.articles)
print('文章数', me.articles_count)
print('头像地址', me.avatar_url)
print('用户所在行业', me.business)
print('收藏数', me.collected_count)
print('收藏夹数', me.collection_count)
print('收藏夹', me.collections)
print('专栏数', me.column_count)
print('专栏', me.columns)
print('专栏数', me.columns_count)
created_at = time.localtime(me.created_at)
print('创建时间', time.strftime("%Y-%m-%d %H:%M:%S", created_at))
print('个人描述', me.description)
print('草稿数', me.draft_count)
print('教育信息', me.educations)
print('邮箱', me.email)
print('职业信息', me.employments)
print('收藏数', me.favorite_count)
print('被收藏数', me.favorited_count)
print('粉丝数', me.follower_count)
print('粉丝', me.followers)
print('关注数', me.following_column_count)
print('关注专栏', me.following_columns)
print('关注数', me.following_count)
print('关注问题数', me.following_question_count)
print('关注问题', me.following_questions)
print('关注话题数', me.following_topic_count)
print('关注话题', me.following_topics)
print('关注', me.followings)
print('友善度', me.friendly_score)
print('性别', me.gender)
print('有每日推荐权限', me.has_daily_recommend_permission)
print('签名', me.headline)
print('用户ID', me.id)
print('是否活跃', me.is_active)
print('是否被禁', me.is_baned)
print('是否绑定新浪账户', me.is_bind_sina)
print('是否被锁', me.is_locked)
print('是否为Moments用户', me.is_moments_user)
print('位置', me.locations)
print('用户名', me.name)
print('提问数', me.question_count)
print('提问', me.questions)
print('分享数', me.shared_count)
print('微博昵称', me.sina_weibo_name)
print('微博地址', me.sina_weibo_url)
print('感谢数', me.thanked_count)
print('用户UID', me.uid)
print('赞同数', me.voteup_count)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
