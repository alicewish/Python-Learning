import time, os, datetime, re, json

start_time = time.time()  # 初始时间戳
print(start_time)

file_dir = '/Users/alicewish/Google 云端硬盘/'

file_list = os.listdir(file_dir)  # 获得目录中的内容
print(file_list)

file_name = "[伦理学导论].（美）弗兰克·梯利.扫描版.gdoc"
file_path = file_dir + file_name
# ================文件信息================
is_dir = os.path.isdir(file_path)  # 判断目标是否目录
extension = os.path.splitext(file_path)[1]  # 拓展名
extension_list=[".gdoc",".gsheet"]
if not is_dir and extension in extension_list:
    last_access_time = datetime.datetime.fromtimestamp(os.path.getatime(file_path))  # 最近访问时间
    created_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))  # 输出文件创建时间
    last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))  # 最近修改时间
    file_size = os.path.getsize(file_path)  # 输出文件大小（字节为单位）
    extension = os.path.splitext(file_path)[1]  # 拓展名

    read_text = open(file_path, 'rb').read()  # 读取文本
    decoded_text = str(read_text)[2:-1]
    data = json.loads(decoded_text)  # 将json字符串转换成python对象
    url = data["url"]
    doc_id = data["doc_id"]
    email = data["email"]
    resource_id = data["resource_id"]
    info = [file_name, str(created_time), str(last_modified_time), str(last_access_time), str(file_size), url, doc_id,
            email, resource_id]
    line = "\t".join(info)
    print(line)
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
