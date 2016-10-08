import time, re,MyDef

start_time = time.time()  # 初始时间戳
now = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳
# ========================输入区开始========================

# ================读取剪贴板================
text_readline = MyDef.ReadClipL()

# ========================处理文本========================

output_readline = []  # 初始化信息列表

for i in range(len(text_readline)):
    line = text_readline[i]
    output_line = line
    level = 1
    if re.match(r'第\w部分', line):
        level = 1
    elif re.match(r'第[0-9]{1,}章', line):
        level = 2
    elif re.match(r'[0-9]{1,2}\.[0-9]{1,2}', line):
        level = 3
    else:
        level = 3
    output_line = (level - 1) * "  " + "- "+line
    output_readline.append(output_line)

# ================写入昵称列表================
text = '\r\n'.join(output_readline)  # 写入文本
print(text)
# ================写入剪贴板================
import pyperclip

pyperclip.copy(text)
spam = pyperclip.paste()

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
