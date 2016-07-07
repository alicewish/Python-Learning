import time, re

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
input_file_name = '扫描规范化测试'  # 输入文件的名称
output_file_name = '扫描规范化测试处理'  # 输出文件的名称

path_prefix = '/Users/alicewish/我的坚果云/'  # 文件地址前缀
input_file_path = path_prefix + input_file_name + '.txt'  # 输入文件的地址
output_file_path = path_prefix + output_file_name + '.txt'  # 输出文件的地址

# ================按行读取文本================
text_readline = []  # 初始化按行存储数据列表
with open(input_file_path) as fin:
    for line in fin:
      this_line=(line.replace('\n', '')).replace('\t','')
      if this_line != '': # 非空
        if re.match(r"[\.?!\"-]", this_line[-1]):  # 结尾若为.?!"
          this_line=this_line+'接'
        text_readline.append(this_line)
print(text_readline)

# ================写入文本================
text = '\r\n'.join(text_readline)
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

