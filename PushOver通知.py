import time
from pushover import Client

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
file_name = 'PushOver'  # 文件名
path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
txt_file_path = path_prefix + file_name + '.txt'  # TXT文件名
# ================按行读取文本:with open(更好)================
text_readline = []  # 初始化按行存储数据列表,不接受结尾换行符
with open(txt_file_path) as fin:
    for line in fin:
        text_readline.append((line).replace('\n', ''))

my_user_key = text_readline[0]
my_api_token = text_readline[1]

client = Client(my_user_key, api_token=my_api_token)
client.send_message("测试内容……" + now, title="标题", sound="cosmic")

# send_message可用关键字包括title, priority, sound, callback, timestamp, url, url_title, device, retry

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
