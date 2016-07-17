import time, json
from collections import OrderedDict

start_time = time.time()  # 初始时间戳
input_file_path = "/Users/alicewish/我的坚果云/图床表.txt"

# ================按行读取参考文本并字典化================
input_dict = {}  # 创建一个字典
with open(input_file_path) as fin:
    for line in fin:
        input_line = (line.replace('\n', ''))
        if "【" in input_line:
            source_name = input_line
            # input_dict[source_name] = {}
        elif "\t" in input_line:  # 接受key value格式
            split_line = input_line.split("\t")
            key = split_line[0].zfill(2)
            value = split_line[1]
            if '<img src="' in value:
                value = value.replace('<img src="', '![](').replace('" />', ')')
            print(source_name, key, value)
            input_dict[source_name][key] = value
            input_dict[source_name] = OrderedDict(input_dict[source_name])
input_dict = OrderedDict(input_dict)

print(input_dict)
line_list = []
for key, value in input_dict.items():
    line_list.append(key)
    print(key)
    for k, v in value.items():
        line_list.append(k + "\t" + v)

info = "\r\n".join(line_list)
# print(info)

# ================写入TXT================
txt_file_path = '/Users/alicewish/我的坚果云/图床表.txt'  # TXT文件名
f = open(txt_file_path, 'w')
try:
    f.write(info)
finally:
    f.close()

f = open('/Users/alicewish/我的坚果云/图床表JSON.txt', 'w')
json.dump(input_dict, f)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
