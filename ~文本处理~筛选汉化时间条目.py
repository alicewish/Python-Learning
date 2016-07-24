import time, os, json

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
input_file_path = "/Users/alicewish/Documents/Timing Export A.csv"
output_file_path = "/Users/alicewish/我的坚果云/Timing Export筛选.csv"

file_dir = '/Users/alicewish/Google 云端硬盘/'
file_list = os.listdir(file_dir)  # 获得目录中的内容
print(file_list)
google_drive_dict = {}
for file_name in file_list:
    file_path = file_dir + file_name
    # ================文件信息================
    is_dir = os.path.isdir(file_path)  # 判断目标是否目录
    extension = os.path.splitext(file_path)[1]  # 拓展名
    extension_list = [".gdoc", ".gsheet", ".gscript"]
    if not is_dir and extension in extension_list:
        read_text = open(file_path, 'rb').read()  # 读取文本
        decoded_text = str(read_text)[2:-1]
        data = json.loads(decoded_text)  # 将json字符串转换成python对象
        url = data["url"]
        doc_id = data["doc_id"]
        email = data["email"]
        resource_id = data["resource_id"]
        google_drive_dict[doc_id] = file_name
# ================按行读取输入文本================
print("开始读取")
read_text = open(input_file_path, 'r').read()  # 读取文本
text_readline = read_text.splitlines()
photoshop_list = [".psd", ".jpg", "/Volumes/Mack/汉化/"]

readline = []  # 初始化按行存储数据列表,不接受换行符
for i in range(len(text_readline)):
    line = text_readline[i]
    status = False
    if "应用程序" in line and "持续时间" in line:
        status = True
    if "Google Chrome" in line:
        for key in google_drive_dict:
            if key in text_readline[i]:
                status = True
    if "Photoshop CC" in line:
        for key in photoshop_list:
            if key in line:
                app_status = True
    if "Quiver" in line:
        status = True
    if "Simple Comic" in line:
        status = True
    if "Snip" in line:
        status = True
    if status:
        print(i)
        readline.append(line)

text = "\r\n".join(readline)
print("总条目", len(readline))

# ================写入文本================

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
