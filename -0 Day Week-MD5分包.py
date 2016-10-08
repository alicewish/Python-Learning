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


def ReadMD5SamplingCSV():
    import os, MyDef
    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5随机分样表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)
    return MyDef.ReadDictB(refer_file_path)


def ChangeBack():
    import os, MyDef
    dropbox_path = '/Users/alicewish/Dropbox'
    refer_file_name = '漫画图源MD5表.csv'
    refer_file_path = os.path.join(dropbox_path, refer_file_name)
    text_readline = MyDef.ReadCSV(refer_file_path, type=False)
    for i in range(len(text_readline)):
        if '@k_k@' in text_readline[i][1]:
            print(text_readline[i][1])
            text_readline[i][1] = text_readline[i][1].replace('@k_k@', '')
    MyDef.StoreCSV(text_readline, refer_file_path)


def Distribute():
    import time, MyDef, os, shutil
    start_time = time.time()  # 初始时间戳
    refer_dict = ReadMD5SamplingCSV()
    MD5_refer_dict, MD5_list = ReadMD5CSV()

    # ========================最外层目录========================
    new_file_dir = '/Volumes/Mack/Distribute'
    if not os.path.exists(new_file_dir):  # 判断目标是否存在
        try:
            os.mkdir(new_file_dir)  # 创建最外层目录
        except:
            pass
    # ========================主目录========================
    for key in refer_dict:
        folder_name = MyDef.HexShift(key)
        new_folder_path = os.path.join(new_file_dir, folder_name)
        if not os.path.exists(new_folder_path):  # 判断目标是否存在
            try:
                os.mkdir(new_folder_path)  # 创建目录
            except:
                pass
        sample_list = refer_dict[key].split("|")
        print(sample_list)
        # ========================次级目录========================
        for sample in sample_list:  # 文件MD5
            file_path = MD5_refer_dict[sample]
            file_name = os.path.split(file_path)[1]
            print("旧", file_path)
            file_folder_name = MyDef.HexShift(sample)

            new_file_folder_path = os.path.join(new_file_dir, folder_name, folder_name + file_folder_name)

            try:
                os.mkdir(new_file_folder_path)  # 创建目录
            except:
                pass

            new_file_path = os.path.join(new_file_folder_path, file_name)
            print("新", new_file_path)

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

    # ========================最外层目录========================
    new_file_dir = '/Volumes/Mack/Distribute'

    # ========================主目录========================
    for key in refer_dict:
        folder_name = MyDef.HexShift(key)
        new_folder_path = os.path.join(new_file_dir, folder_name)

        sample_list = refer_dict[key].split("|")
        print(sample_list)
        # ========================次级目录========================
        for sample in sample_list:  # 文件MD5
            file_path = MD5_refer_dict[sample]
            file_name = os.path.split(file_path)[1]
            print("旧", file_path)
            file_folder_name = MyDef.HexShift(sample)

            new_file_folder_path = os.path.join(new_file_dir, folder_name, folder_name + file_folder_name)

            new_file_path = os.path.join(new_file_folder_path, file_name)
            print("新", new_file_path)

            try:
                shutil.move(new_file_path, file_path)  # 移动文件或目录都是使用这条命令
            except:
                pass

    print(MyDef.RunTime(start_time))


UnDistribute()
