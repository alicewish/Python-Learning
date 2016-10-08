import time, re, MyDef

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
refer_file_path = "/Users/alicewish/我的坚果云/图床.txt"  # 词典文件的地址
input_file_path = "/Users/alicewish/Downloads/my.md"

read_text = open(input_file_path, 'r').read()  # 读取文本
# ================按行读取参考文本并字典化================
refer_dict = {}  # 创建一个字典
with open(refer_file_path) as fin:
    for line in fin:
        refer_line = line.replace('\n', '')
        if "\t" in refer_line:  # 接受key value格式
            split_line = refer_line.split("\t")
            refer_dict[split_line[0].zfill(2)] = split_line[1].replace('<img src="', '![](').replace('" />', ')')

# ================按行读取输入文本================

text_readline = read_text.replace("\nclass", "class").splitlines()
print(text_readline)
readline = []  # 初始化按行存储数据列表,不接受换行符
for i in range(len(text_readline)):
    raw = text_readline[i]
    text_readline[i] = re.sub(r'<span.*</span>', '', raw)
    key = text_readline[i]
    if key in refer_dict:
        text_readline[i] = refer_dict[key]
    readline.append(text_readline[i])

text = "\r\n".join(readline)
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
