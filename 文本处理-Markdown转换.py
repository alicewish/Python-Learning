from lxml import html
import requests, time, re, shutil

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_name="应用推荐-Simple Comic——Mac看漫画必备.md"
input_file_path_prefix = "/Users/alicewish/Documents/GitHub/Writing/"
output_file_path_prefix = "/Users/alicewish/Documents/GitHub/Writing/Modified/"
input_file_path=input_file_path_prefix+file_name
output_file_path=output_file_path_prefix+file_name
new_path = "/Users/alicewish/Pictures/往期/"
# ================按行读取输入文本================
input_readline = []  # 初始化按行存储数据列表,不接受换行符
output_readline = []  # 初始化按行存储数据列表

with open(input_file_path) as fin:
    for line in fin:
        this_line = line.replace('\n', '')
        if "![" in this_line:
            # ========================执行区开始========================
            pattern = re.compile(r'!\[.*\]\(/Users/.*\)')
            # 使用Pattern匹配文本，获得全部匹配结果
            find = pattern.findall(this_line)  # 列表形式存储的结果
            old_pic_line=find[0]
            pattern_inside = re.compile(r'\(/Users/.*\)')
            path_find = pattern_inside.findall(old_pic_line)  # 列表形式存储的结果
            ab_path=path_find[0].strip("()")
            new_pic_line="!["+ab_path+"]("+ab_path+")"
            try:
                shutil.copy(ab_path, new_path)
            except:
                pass
            this_line=new_pic_line
        output_readline.append(this_line)

# ================写入文本================
text = '\r\n'.join(output_readline)
print(text)

f = open(output_file_path, 'w')
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
