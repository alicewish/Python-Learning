from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ============评论模块============
cid = 10000
comment = client.comment(cid)
print('允许删除', comment.allow_delete)
print('允许喜欢', comment.allow_like)
print('允许回复', comment.allow_reply)
print('先祖', comment.ancestor)
print('作者', comment.author)
print('内容', comment.content)
print('对话', comment.conversation)
print('创建时间', comment.created_time)
print('评论ID', comment.id)
print('是否是答案/文章/etc的作者的评论。', comment.is_author)
print('是否被删除', comment.is_delete)
print('是否是答案/文章/etc的作者的评论。', comment.is_parent_author)
print('回复本条评论的所有评论的列表（生成器）', comment.replies)
print('获取这条评论的父评论的作者，如果并没有回复谁则返回 None', comment.reply_to)
print('是对什么东西的评论', comment.resource_type)
print('赞同数', comment.vote_count)
print('是否点赞了', comment.voting)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
