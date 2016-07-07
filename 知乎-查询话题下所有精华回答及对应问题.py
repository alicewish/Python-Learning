import time

start_time = time.time()  # 初始时间戳

# ========================登录========================
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
client.load_token('/Users/alicewish/我的坚果云/token.pkl')

# ==================查询话题下所有精华回答及对应问题==================
tid = 19559937  # 留学
topic = client.topic(tid)
topic_name = topic.name
question_line = []
# ==================所有精华回答==================
for answer in topic.best_answers:
    entry_start_time = time.time()  # 每条起始时间戳
    author = answer.author
    can_comment = answer.can_comment
    collections = answer.collections
    comment_count = answer.comment_count
    comment_permission = answer.comment_permission
    comments = answer.comments
    content = answer.content
    created_time = answer.created_time
    excerpt = answer.excerpt
    answer_id = answer.id
    is_copyable = answer.is_copyable
    is_mine = answer.is_mine
    suggest_edit = answer.suggest_edit
    thanks_count = answer.thanks_count
    answer_updated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(answer.updated_time))
    voters = answer.voters
    voteup_count = answer.voteup_count
    # ==================对应问题==================
    question = answer.question
    answer_count = question.answer_count
    detail = question.detail
    excerpt = question.excerpt
    follower_count = question.follower_count
    question_id = question.id
    title = question.title
    question_updated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(question.updated_time))

    # 整理
    question_info = [str(answer_id), str(voteup_count), answer_updated_time, str(question_id), title, detail, excerpt,
                     question_updated_time]
    info_line = '\t'.join(question_info)
    print(info_line)
    question_line.append(info_line)
    # 合并数据
    text = '\r\n'.join(question_line)
    entry_run_time = time.time() - entry_start_time
    print("耗时:{:.2f}秒".format(entry_run_time))
    # ================写入TXT================
    txt_file_path = '/Users/alicewish/我的坚果云/查询' + topic_name + '话题下所有精华回答及对应问题.txt'  # TXT文件名
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
