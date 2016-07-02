import time

start_time = time.time()  # 初始时间戳

from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

file_name = '知乎'  # 文件名
path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名
# ================按行读取文本================
text_readline = []  # 初始化按行存储数据列表,不接受结尾换行符
with open(txt_file_path) as fin:
    for line in fin:
        text_readline.append((line).replace('\n', ''))
print(text_readline)

for i in range(len(text_readline)):
    print(text_readline[i])
# ================读取账号和密码================
account = text_readline[0]
passward = text_readline[1]

client = ZhihuClient()

try:
    client.login(account, passward)
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login(account, passward, captcha)

# 必须在 client 已经处于登录状态时才能使用
client.save_token('/Users/alicewish/我的坚果云/token.pkl')

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
