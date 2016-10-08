import time, os, shutil, MyDef

start_time = time.time()  # 初始时间戳
# ========================输入区开始========================
out_file_dir = '/Volumes/Mack/~Week 0-Day/'
now_date = time.strftime("%Y%m%d", time.localtime())  # 当前日期戳

dropbox_path = '/Users/alicewish/Dropbox'

output_readline = []
markdown_readline = []

url_dict_file_name = '度盘分享地址.txt'
url_dict_file_path = os.path.join(dropbox_path, url_dict_file_name)

# ================按行读取审查关键词并字典化================
url_dict = {}  # 创建一个字典
with open(url_dict_file_path) as fin:
    for line in fin:
        refer_line = (line.replace('\n', '')).replace('\t', '')
        if "|" in refer_line:  # 接受key|value格式
            split_line = refer_line.split("|")
            url_dict[split_line[0]] = split_line[1]

# ================读取外文件夹内容================
out_file_list = os.listdir(out_file_dir)  # 获得目录中的内容

for dir_name in out_file_list:
    file_dir = os.path.join(out_file_dir, dir_name)
    try:
        url = url_dict[dir_name]
        print(file_dir)
        # ================读取内文件夹内容================
        file_list = os.listdir(file_dir)  # 获得目录中的内容

        # ================计数器初始化================
        file_count = len(file_list)
        print("文件数", file_count)

        # ================记录文件================
        for file_name in file_list:
            file_path = os.path.join(file_dir, file_name)
            output_line_in_list = ['"' + file_name + '"', '"' + url + '"', '"' + dir_name + '"']
            output_line = ",".join(output_line_in_list)
            output_readline.append(output_line)

            markdown_line = file_name + " | [" + dir_name + "](" + url + ")"
            markdown_readline.append(markdown_line)
    except:
        # url = '暂未分享成功(' + dir_name + ')'
        url = dir_name
        print(file_dir)
        # ================读取内文件夹内容================
        file_list = os.listdir(file_dir)  # 获得目录中的内容

        # ================计数器初始化================
        file_count = len(file_list)
        print("文件数", file_count)

        # ================记录文件================
        for file_name in file_list:
            file_path = os.path.join(file_dir, file_name)
            output_line_in_list = ['"' + file_name + '"', '"' + url + '"', '"' + dir_name + '"']
            output_line = ",".join(output_line_in_list)
            output_readline.append(output_line)

            markdown_line = file_name + " | " + url
            markdown_readline.append(markdown_line)

output_readline.sort()
output_readline = ['"File Name","Download Link","Folder"'] + output_readline

markdown_readline.sort()
markdown_readline = ['文件名 | 下载地址', '--- | ---'] + markdown_readline
# ================写入文本================
all_count = len(output_readline) - 1
print(all_count)
text = '\r\n'.join(output_readline)
# print(text)

output_file_name = '0 Day Week文件地址-墨问非名制作-' + now_date + '(' + str(all_count) + ').csv'

output_file_path = os.path.join(dropbox_path, output_file_name)
f = open(output_file_path, 'w')
try:
    f.write(text)
finally:
    f.close()

# ================写入剪贴板================
markdown_text = '\r\n'.join(markdown_readline)

MyDef.WriteClip(markdown_text)

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
