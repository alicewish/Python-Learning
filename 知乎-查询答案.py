from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ========================查询答案========================
aid = 34404209
answer = client.answer(aid)
print('作者', answer.author)
print('能否评论', answer.can_comment)
print('收藏夹', answer.collections)
print('评论数', answer.comment_count)
print('评论权限', answer.comment_permission)
print('评论', answer.comments)
print('内容', answer.content)
print('创建时间', answer.created_time)
print('摘录', answer.excerpt)
print('答案ID', answer.id)
print('能否复制', answer.is_copyable)
print('是我回答的吗', answer.is_mine)
print('从属问题', answer.question)
print('建议修改', answer.suggest_edit)
print('感谢数', answer.thanks_count)
print('更新时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(answer.updated_time)))
print('投票者', answer.voters)
print('赞同数', answer.voteup_count)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
