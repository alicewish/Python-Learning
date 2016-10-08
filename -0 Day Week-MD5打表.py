# ========================函数区开始========================
def MD5Table(file_dir):
    import time, os, MyDef
    start_time = time.time()  # 初始时间戳
    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)  # 词典文件的地址
    MD5_refer_dict = MyDef.ReadDictB(refer_file_path, True)
    # print(MD5_refer_dict)
    file_path_check_set = set()
    major_key_list = []
    output_list = []
    # ================读取文件夹内容================
    file_list = os.listdir(file_dir)  # 获得目录中的内容
    # print(file_list)

    for file_MD5 in MD5_refer_dict:
        file_path = MD5_refer_dict[file_MD5]
        file_path_check_set.add(file_path)

    for file_name in file_list:
        file_path = os.path.join(file_dir, file_name)
        if file_path in file_path_check_set:
            pass
        else:
            # file_MD5 = MyDef.HashMD5File(file_path)
            file_MD5 = MyDef.md5sum(file_path)
            print(file_MD5, file_name)
            MD5_refer_dict[file_MD5] = file_path

    for file_MD5 in MD5_refer_dict:
        file_path = MD5_refer_dict[file_MD5]
        file_name = os.path.split(file_path)[1]
        major_key = file_name + file_MD5
        major_key_list.append(major_key)

    major_key_list.sort()
    for major_key in major_key_list:
        file_MD5 = major_key[-32:]
        info_list = [file_MD5, MD5_refer_dict[file_MD5]]
        output_list.append(info_list)
    head_info = ['MD5', '路径']
    MyDef.StoreCSV(output_list, refer_file_path, head_info)
    print(MyDef.RunTime(start_time))


# file_dir = '/Volumes/Mack/~Week 0-Day/0-Day Week of 2016.09.14'



import os

out_file_dir = '/Volumes/Mack/~Week 0-Day/'
# ================读取外文件夹内容================
out_file_list = os.listdir(out_file_dir)  # 获得目录中的内容

for dir_name in out_file_list:
    file_dir = os.path.join(out_file_dir, dir_name)
    MD5Table(file_dir)
