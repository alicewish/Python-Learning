from lxml import html
import requests, time, zhihu_oauth

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ============文章模块============
aid = 10000
article = client.article(aid)
print('作者', article.author)
print('能否评论', article.can_comment)
print('从属专栏', article.column)
print('评论数', article.comment_count)
print('评论权限', article.comment_permission)
print('评论', article.comments)
print('内容', article.content)
print('摘录', article.excerpt)
print('文章ID', article.id)
print('图像地址', article.image_url)
print('建议修改', article.suggest_edit)
print('标题', article.title)
print('更新时间', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(article.updated_time)))
print('赞同数', article.voteup_count)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
