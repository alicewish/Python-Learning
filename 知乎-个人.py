from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ========================我========================
me = client.me()
# print('活动', me.activities)
# print('答案数', me.answer_count)
# print('答案', me.answers)
# print('文章', me.articles)
# print('文章数', me.articles_count)
# print('头像地址', me.avatar_url)
# print('用户所在行业', me.business)
# print('收藏数', me.collected_count)
# print('收藏夹数', me.collection_count)
# print('收藏夹', me.collections)
# print('专栏数', me.column_count)
# print('专栏', me.columns)
# print('专栏数', me.columns_count)
# created_at = time.localtime(me.created_at)
# print('创建时间', time.strftime("%Y-%m-%d %H:%M:%S", created_at))
# print('个人描述', me.description)
# print('草稿数', me.draft_count)
# print('教育信息', me.educations)
# print('邮箱', me.email)
# print('职业信息', me.employments)
# print('收藏数', me.favorite_count)
# print('被收藏数', me.favorited_count)
# print('粉丝数', me.follower_count)
# print('粉丝', me.followers)
# print('关注数', me.following_column_count)
# print('关注专栏', me.following_columns)
# print('关注数', me.following_count)
# print('关注问题数', me.following_question_count)
# print('关注问题', me.following_questions)
# print('关注话题数', me.following_topic_count)
# print('关注话题', me.following_topics)
# print('关注', me.followings)
# print('友善度', me.friendly_score)
# print('性别', me.gender)
# print('有每日推荐权限', me.has_daily_recommend_permission)
# print('签名', me.headline)
# print('用户ID', me.id)
# print('是否活跃', me.is_active)
# print('是否被禁', me.is_baned)
# print('是否绑定新浪账户', me.is_bind_sina)
# print('是否被锁', me.is_locked)
# print('是否为Moments用户', me.is_moments_user)
# print('位置', me.locations)
# print('用户名', me.name)
# print('提问数', me.question_count)
# print('提问', me.questions)
# print('分享数', me.shared_count)
# print('微博昵称', me.sina_weibo_name)
# print('微博地址', me.sina_weibo_url)
# print('感谢数', me.thanked_count)
# print('用户UID', me.uid)
# print('赞同数', me.voteup_count)

# # ========================查询他人========================
# pid = "edna-krabappel"
# people = client.people(pid)
#
# people = client.people(pid)
# print('活动', people.activities)
# print('答案数', people.answer_count)
# print('答案', people.answers)
# print('文章', people.articles)
# print('文章数', people.articles_count)
# print('头像地址', people.avatar_url)
# print('用户所在行业', people.business)
# print('收藏数', people.collected_count)
# print('收藏夹数', people.collection_count)
# print('收藏夹', people.collections)
# print('专栏数', people.column_count)
# print('专栏', people.columns)
# print('专栏数', people.columns_count)
# then = time.localtime(people.created_at)
# print('创建时间', time.strftime("%Y-%m-%d %H:%M:%S", then))
# print('个人描述', people.description)
# print('草稿数', people.draft_count)
# print('教育信息', people.educations)
# print('邮箱', people.email)
# print('职业信息', people.employments)
# print('收藏数', people.favorite_count)
# print('被收藏数', people.favorited_count)
# print('粉丝数', people.follower_count)
# print('粉丝', people.followers)
# print('关注数', people.following_column_count)
# print('关注专栏', people.following_columns)
# print('关注数', people.following_count)
# print('关注问题数', people.following_question_count)
# print('关注问题', people.following_questions)
# print('关注话题数', people.following_topic_count)
# print('关注话题', people.following_topics)
# print('关注', people.followings)
# print('友善度', people.friendly_score)
# print('性别', people.gender)
# print('有每日推荐权限', people.has_daily_recommend_permission)
# print('签名', people.headline)
# print('用户ID', people.id)
# print('是否活跃', people.is_active)
# print('是否被禁', people.is_baned)
# print('是否绑定新浪账户', people.is_bind_sina)
# print('是否被锁', people.is_locked)
# print('是否为Moments用户', people.is_moments_user)
# print('位置', people.locations)
# print('用户名', people.name)
# print('提问数', people.question_count)
# print('提问', people.questions)
# print('分享数', people.shared_count)
# print('微博昵称', people.sina_weibo_name)
# print('微博地址', people.sina_weibo_url)
# print('感谢数', people.thanked_count)
# print('用户UID', people.uid)
# print('赞同数', people.voteup_count)

# # ========================查询问题========================
# qid = 22384666
# question = client.question(qid)
# print('允许删除', question.allow_delete)
# print('答案数', question.answer_count)
# print('答案', question.answers)
# print('评论数', question.comment_count)
# print('评论', question.comments)
# print('细节', question.detail)
# print('摘录', question.excerpt)
# print('关注数', question.follower_count)
# print('关注人', question.followers)
# print('问题ID', question.id)
# print('重定向', question.redirection)
# print('状态', question.status)
# print('建议修改', question.suggest_edit)
# print('标题', question.title)
# print('话题', question.topics)
# print('更新时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(question.updated_time)))
#
# # # ========================查询话题========================
# tid = 19668865
# topic = client.topic(tid)
# print('图标地址', topic.avatar_url)
# print('最佳回答数', topic.best_answer_count)
# print('最佳回答者', topic.best_answerers)
# print('精华回答', topic.best_answers)
# print('精华回答数', topic.best_answers_count)
# print('子话题详情', topic.children)
# print('摘录', topic.excerpt)
# print('父话题数', topic.father_count)
# print('关注人数', topic.follower_count)
# print('关注人', topic.followers)
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

# ==================查询话题下所有未回答问题==================
tid = 19668865
topic = client.topic(tid)
question_line = []
for question in topic.unanswered_questions:
    entry_start_time = time.time()
    allow_delete = question.allow_delete
    answer_count = question.answer_count
    answers = question.answers
    comment_count = question.comment_count
    comments = question.comments
    detail = question.detail
    excerpt = question.excerpt
    follower_count = question.follower_count
    followers = question.followers
    id = question.id
    redirection = question.redirection
    status = question.status
    suggest_edit = question.suggest_edit
    title = question.title
    topics = question.topics
    updated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(question.updated_time))
    # 整理
    question_info = [title, detail, excerpt, str(follower_count), str(id), updated_time]
    info_line = '\t'.join(question_info)
    print(info_line)
    question_line.append(info_line)
    # 合并数据
    text = '\r\n'.join(question_line)
    entry_run_time = time.time() - entry_start_time
    print("耗时:{:.2f}秒".format(entry_run_time))
    # time.sleep(3)
    # ================写入TXT================
    txt_file_path = '/Users/alicewish/我的坚果云/查询DC Comics话题下所有未回答问题.txt'  # TXT文件名
    f = open(txt_file_path, 'w')
    try:
        f.write(text)
    finally:
        f.close()

# # ================写入剪贴板================
# import pyperclip
#
# pyperclip.copy(text)
# spam = pyperclip.paste()

# # ==================查询话题下所有精华回答者==================
# tid = 19668865
# topic = client.topic(tid)
# answerers_line = []
# for follower in topic.best_answerers:
#     # 查询所有可用信息
#     activities = follower.activities
#     answer_count = follower.answer_count
#     answers = follower.answers
#     articles = follower.articles
#     articles_count = follower.articles_count
#     avatar_url = follower.avatar_url
#     business = follower.business
#     collected_count = follower.collected_count
#     collection_count = follower.collection_count
#     collections = follower.collections
#     column_count = follower.column_count
#     columns = follower.columns
#     columns_count = follower.columns_count
#     created_at = follower.created_at
#     description = ((follower.description).replace("\t","")).replace("\n","|") #清理会打乱数据的换行和制表符
#     draft_count = follower.draft_count
#     educations = follower.educations
#     email = follower.email
#     employments = follower.employments
#     favorite_count = follower.favorite_count
#     favorited_count = follower.favorited_count
#     follower_count = follower.follower_count
#     followers = follower.followers
#     following_column_count = follower.following_column_count
#     following_columns = follower.following_columns
#     following_count = follower.following_count
#     following_question_count = follower.following_question_count
#     following_questions = follower.following_questions
#     following_topic_count = follower.following_topic_count
#     following_topics = follower.following_topics
#     followings = follower.followings
#     friendly_score = follower.friendly_score
#     gender = follower.gender
#     has_daily_recommend_permission = follower.has_daily_recommend_permission
#     headline = follower.headline
#     id = follower.id
#     is_active = follower.is_active
#     is_baned = follower.is_baned
#     is_bind_sina = follower.is_bind_sina
#     is_locked = follower.is_locked
#     is_moments_user = follower.is_moments_user
#     locations = follower.locations
#     name = follower.name
#     question_count = follower.question_count
#     questions = follower.questions
#     shared_count = follower.shared_count
#     sina_weibo_name = follower.sina_weibo_name
#     sina_weibo_url = follower.sina_weibo_url
#     thanked_count = follower.thanked_count
#     uid = follower.uid
#     voteup_count = follower.voteup_count
#     # 整理
#     follower_info = [name, str(gender), str(voteup_count), str(follower_count), str(answer_count), str(articles_count),str(description), str(headline), str(email), str(sina_weibo_name), str(sina_weibo_url)]
#     info_line = '\t'.join(follower_info)
#     print(info_line)
#     answerers_line.append(info_line)
# # 合并数据
# text = '\r\n'.join(answerers_line)
#
# # ================写入剪贴板================
# import pyperclip
# pyperclip.copy(text)
# spam = pyperclip.paste()
# # ========================查询答案========================
# aid = 34404209
# answer = client.answer(aid)
# print('作者', answer.author)
# print('能否评论', answer.can_comment)
# print('收藏夹', answer.collections)
# print('评论数', answer.comment_count)
# print('评论权限', answer.comment_permission)
# print('评论', answer.comments)
# # print('内容', answer.content)
# print('创建时间', answer.created_time)
# print('摘录', answer.excerpt)
# print('答案ID', answer.id)
# print('能否复制', answer.is_copyable)
# print('是我回答的吗', answer.is_mine)
# print('从属问题', answer.question)
# print('建议修改', answer.suggest_edit)
# print('感谢数', answer.thanks_count)
# print('更新时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(answer.updated_time)))
# print('投票者', answer.voters)
# print('赞同数', answer.voteup_count)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
