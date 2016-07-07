import requests, time, json

start_time = time.time()  # 初始时间戳
# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()
text_readline = read_text.splitlines()  # 对数据分行
print(text_readline)

line = []
for i in range(len(text_readline)):
    entry_start_time = time.time()
    try:
        # ========================获取对应Hash========================
        html = requests.get('http://api.kanzhihu.com/searchuser/' + text_readline[i])
        data = json.loads(html.text)  # 将json字符串转换成python对象
        users = data['users']
        first_user = users[0]
        user_hash = first_user['hash']
        print(user_hash)
        line.append(user_hash)
    except:
        line.append("")
    line_text = '\r\n'.join(line)
    # ================每项时间计时================
    entry_run_time = time.time() - entry_start_time
    entry_print = "耗时:{:.4f}秒".format(entry_run_time)
    print(entry_print)

# ================写入剪贴板================
import pyperclip

pyperclip.copy(line_text)
spam = pyperclip.paste()

# ================写入TXT================
txt_file_path = '/Users/alicewish/我的坚果云/批量查询用户Hash.txt'  # TXT文件名
f = open(txt_file_path, 'w')
try:
    f.write(line_text)
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
