# ========================函数区开始========================

def RandomSample(MD5_list, number=10):
    import random
    if number < len(MD5_list):
        random_sample = random.sample(MD5_list, number)
    else:
        random_sample = MD5_list
    print(random_sample)
    random_sample.sort()
    remain_sample = list(set(MD5_list).difference(set(random_sample)))
    return (random_sample, remain_sample)


def ReadMD5CSV():
    import os, MyDef
    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)  # 词典文件的地址
    MD5_refer_dict = MyDef.ReadDictC(refer_file_path, True)

    MD5_list = []
    for file_MD5 in MD5_refer_dict:
        MD5_list.append(file_MD5)
    return (MD5_refer_dict, MD5_list)


# ========================输入区开始========================

def Sampling(number=30):
    import time, MyDef, os

    start_time = time.time()  # 初始时间戳

    MD5_refer_dict, MD5_list = ReadMD5CSV()

    remain_sample = MD5_list
    refer_dict = {}
    while len(remain_sample) > 0:
        random_sample, remain_sample = RandomSample(remain_sample, number)
        random_sample_string = '|'.join(random_sample)
        print(random_sample_string)
        random_sample_string_MD5 = MyDef.HashMD5String(random_sample_string)
        print('方案MD5', random_sample_string_MD5)
        refer_dict[random_sample_string_MD5] = random_sample_string

    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5随机分样表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)
    MyDef.WriteDictB(refer_dict, refer_file_path)

    print(MyDef.RunTime(start_time))


# file_dir = '/Volumes/Mack/~Week 0-Day/0-Day Week of 2016.09.14'



# import os
#
# out_file_dir = '/Volumes/Mack/~Week 0-Day/'
# # ================读取外文件夹内容================
# out_file_list = os.listdir(out_file_dir)  # 获得目录中的内容
#
# for dir_name in out_file_list:
#     file_dir = os.path.join(out_file_dir, dir_name)
#     MD5Table(file_dir)



# new_file_path = os.path.join(new_file_dir, m_dir_name, n_dir_name, new_file_name)
# shutil.move(file_path, new_file_path)  # 移动文件或目录都是使用这条命令


# # ================建立分目录================
# new_file_dir = os.path.join(dropbox_path, refer_file_name)
# try:
#     os.mkdir(new_file_dir)  # 创建目录
# except:
#     pass
#
# sample = ['a', 'b', 'c', 'd']
# random_sample = random.sample(sample, 3)
#
# # ================移动文件并记录================
# i = 0

# Sampling(50)
def ReadMD5SamplingCSV():
    import os, MyDef
    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5随机分样表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)
    return MyDef.ReadDictB(refer_file_path)


def Distribute():
    import time, MyDef, os, shutil
    start_time = time.time()  # 初始时间戳
    refer_dict = ReadMD5SamplingCSV()
    MD5_refer_dict, MD5_list = ReadMD5CSV()
    new_file_dir = '/Volumes/Mack/Distribute'
    try:
        os.mkdir(new_file_dir)  # 创建目录
    except:
        pass
    for key in refer_dict:
        new_folder_path = os.path.join(new_file_dir, key)

        try:
            os.mkdir(new_folder_path)  # 创建目录
        except:
            pass
        sample_list = refer_dict[key].split("|")
        print(sample_list)
        for sample in sample_list:
            file_path = MD5_refer_dict[sample]
            file_name = os.path.split(file_path)[1]
            print("旧", file_path)
            new_file_path = os.path.join(new_folder_path, sample, file_name)
            print("新", new_file_path)

            new_file_folder_path = os.path.join(new_file_dir, key, sample)

            try:
                os.mkdir(new_file_folder_path)  # 创建目录
            except:
                pass

            try:
                shutil.move(file_path, new_file_path)  # 移动文件或目录都是使用这条命令
            except:
                pass

    print(MyDef.RunTime(start_time))


def UnDistribute():
    import time, MyDef, os, shutil
    start_time = time.time()  # 初始时间戳
    refer_dict = ReadMD5SamplingCSV()
    MD5_refer_dict, MD5_list = ReadMD5CSV()
    new_file_dir = '/Volumes/Mack/Distribute'

    for key in refer_dict:
        new_folder_path = os.path.join(new_file_dir, key)

        sample_list = refer_dict[key].split("|")
        print(sample_list)
        for sample in sample_list:
            file_path = MD5_refer_dict[sample]
            file_name = os.path.split(file_path)[1]
            print("旧", file_path)
            new_file_path = os.path.join(new_folder_path, sample, file_name)
            print("新", new_file_path)

            try:
                shutil.move(new_file_path, file_path)  # 移动文件或目录都是使用这条命令
            except:
                pass

    print(MyDef.RunTime(start_time))


Distribute()
