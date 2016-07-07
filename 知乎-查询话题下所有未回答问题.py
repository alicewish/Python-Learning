import time

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ==================查询话题下所有未回答问题==================
tid = 19550921  # 时间管理
topic = client.topic(tid)
topic_name = topic.name
question_line = []
for question in topic.unanswered_questions:
    entry_start_time = time.time()  # 每条起始时间戳
    allow_delete = question.allow_delete
    answer_count = question.answer_count
    answers = question.answers
    comment_count = question.comment_count
    comments = question.comments
    detail = (question.detail).replace("\t", "").replace("\n", "|")
    excerpt = (question.excerpt).replace("\t", "").replace("\n", "|")
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
    # ================写入TXT================
    txt_file_path = '/Users/alicewish/我的坚果云/查询' + topic_name + '话题下所有未回答问题.txt'  # TXT文件名
    f = open(txt_file_path, 'w')
    try:
        f.write(text)
    finally:
        f.close()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
