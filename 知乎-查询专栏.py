from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ============专栏模块============
cid = 10000
column = client.column(cid)
print('文章数', column.article_count)
print('文章', column.articles)
print('文章数', column.articles_count)
print('作者', column.author)
print('能否评论', column.comment_permission)
print('描述', column.description)
print('关注人数', column.follower_count)
print('关注人', column.followers)
print('问题ID', column.id)
print('图像地址', column.image_url)
print('标题', column.title)
print('是否更新过', column.updated)
print('更新时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(column.updated_time)))

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
