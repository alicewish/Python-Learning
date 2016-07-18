import time, json
from collections import OrderedDict

start_time = time.time()  # 初始时间戳
input_file_path = "/Users/alicewish/我的坚果云/图床表HTML.txt"
output_file_path = '/Users/alicewish/我的坚果云/图床表Markdown.txt'  # TXT文件名

# ================按行读取参考文本并字典化================
input_dict = {}  # 创建一个字典
title_list = []
with open(input_file_path) as fin:
    for line in fin:
        input_line = (line.replace('\n', ''))
        if "【" in input_line:
            title_name = input_line
            title_list.append(title_name)
            input_dict[title_name] = {}
        elif "\t" in input_line:  # 接受key value格式
            split_line = input_line.split("\t")
            key = split_line[0].zfill(2)
            markdown_value = split_line[1]
            if '<img src="' in markdown_value:
                markdown_value = markdown_value.replace('<img src="', '![](').replace('" />', ')')
            input_dict[title_name][key] = markdown_value
            input_dict[title_name] = OrderedDict(input_dict[title_name])

input_dict = OrderedDict(input_dict)
print(input_dict)

# ================写入TXT================
markdown_line_list = []
html_line_list = []
title_list.sort()
for title_name in title_list:
    markdown_line_list.append(title_name)
    html_line_list.append(title_name)
    for k, v in input_dict[title_name].items():
        markdown_line_list.append(k + "\t" + v)
        html_value = v.replace('![](', '<img src="').replace(')', '" />')
        html_line_list.append(k + "\t" + html_value)

info = "\r\n".join(markdown_line_list)
f = open(output_file_path, 'w')
try:
    f.write(info)
finally:
    f.close()

info = "\r\n".join(html_line_list)
f = open(input_file_path, 'w')
try:
    f.write(info)
finally:
    f.close()

# f = open('/Users/alicewish/我的坚果云/图床表JSON.txt', 'w')
# json.dump(input_dict, f)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
