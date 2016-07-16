import time, os, shutil

start_time = time.time()  # 初始时间戳

file_dir = '/Users/alicewish/Documents/GitHub/Writing/_posts/Notes/'
new_file_dir = '/Users/alicewish/Documents/GitHub/Writing/_posts/'

file_list = os.listdir(file_dir)  # 获得目录中的内容
print(file_list)

for file_name in file_list:
    file_path = file_dir + file_name
    read_text = open(file_path, 'r').read()
    output_text = read_text.replace("\n", "\r\n")
    f = open(file_path, 'w')
    try:
        f.write(output_text)
    finally:
        f.close()
    new_file_path = new_file_dir + file_name
    shutil.move(file_path, new_file_path)  # 文件或目录都是使用这条命令
os.rmdir(file_dir)  # 只能删除空目录

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
