from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
file_path_prefix = "/Users/alicewish/Documents/GitHub/Writing/"
refer_file_path="/Users/alicewish/我的坚果云/Markdown文件列表.txt"
output_file_path = "/Users/alicewish/我的坚果云/图片地址.txt"  # 输出文件的地址

# ================按行读取参考文本================
refer_readline = []  # 初始化按行存储数据列表,不接受换行符
with open(refer_file_path) as fin:
    for line in fin:
        input_file_path=line.replace('\n', '')
        # ========================执行区开始========================
        read_text = open(input_file_path, 'r').read()  # 读取文本
        pattern = re.compile(r'!\[.*\]\(/Users/.*\)')
        # 使用Pattern匹配文本，获得全部匹配结果
        find = pattern.findall(read_text)#列表形式存储的结果
        print(find)
        # ================写入文本================
        text = '\r\n'.join(find)
        print(text)

        f = open(output_file_path, 'a')
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
