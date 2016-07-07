from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ========================查询问题========================
qid = 48217184
question = client.question(qid)
print('允许删除', question.allow_delete)
print('答案数', question.answer_count)
print('答案', question.answers)
print('评论数', question.comment_count)
print('评论', question.comments)
print('细节', question.detail)
print('摘录', question.excerpt)
print('关注数', question.follower_count)
print('关注人', question.followers)
print('问题ID', question.id)
print('重定向', question.redirection)
print('状态', question.status)
print('建议修改', question.suggest_edit)
print('标题', question.title)
print('话题', question.topics)
print('更新时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(question.updated_time)))

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
