from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ============收藏夹模块============
cid = 10000
collection = client.collection(cid)
print('答案数', collection.answer_count)
print('答案', collection.answers)
print('评论数', collection.comment_count)
print('评论', collection.comments)
print('创建时间', collection.created_time)
print('创建者', collection.creator)
print('描述', collection.description)
print('关注人数', collection.follower_count)
print('关注人', collection.followers)
print('收藏夹ID', collection.id)
print('是否公开', collection.is_public)
print('标题', collection.title)
print('更新时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(collection.updated_time)))

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
