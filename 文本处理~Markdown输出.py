from lxml import html
import requests, time, re

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
output_line = '给你。可口又凉爽。'
output_line_format_list = [0, 0, 0, 0, 0, 0, 3, 3, 3]  # 9
output_line_mark_count_list = []

format_list_for_use = [0] + output_line_format_list + [0]  # 11
for b in range(len(format_list_for_use) - 1):
    output_line_mark_count = abs(format_list_for_use[b + 1] - format_list_for_use[b])
    output_line_mark_count_list.append(output_line_mark_count)

print(output_line_mark_count_list)  # 10

output_markdown_line = ''

for c in range(len(output_line_mark_count_list) - 1):
    for d in range(output_line_mark_count_list[c]):
        output_markdown_line += '*'
    output_markdown_line += output_line[c]

for d in range(output_line_mark_count_list[-1]):
    output_markdown_line += '*'

print(output_markdown_line)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
