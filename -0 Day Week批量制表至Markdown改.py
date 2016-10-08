def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def FileWithLink():
    import time, os, MyDef

    start_time = time.time()  # 初始时间戳
    # ========================输入区开始========================
    output_readline = []

    refer_file_path = '/Users/alicewish/Dropbox/漫画图源MD5表.csv'
    MD5_dict = MyDef.ReadDictC(refer_file_path, True)
    yun_link_file_path = '/Users/alicewish/Dropbox/漫画图源度盘地址表.csv'
    yun_link_dict = MyDef.ReadDictB(yun_link_file_path)

    file_path_list = []
    for key in MD5_dict:
        file_path = MD5_dict[key]
        file_size = os.path.getsize(file_path)
        readable_file_size = sizeof_fmt(file_size)
        file_name = os.path.split(file_path)[1]
        file_path_list.append(file_path)

        if file_path in yun_link_dict:
            yun_link = yun_link_dict[file_path]
            output_line = "[" + file_name + "](" + yun_link + ") | " + readable_file_size
        else:
            output_line = "[" + file_name + "]() | " + readable_file_size
            print(file_name)
        # print(output_line)
        output_readline.append(output_line)
    output_readline.sort()
    output_readline.insert(0, '--- | ---')
    output_readline.insert(0, '文件名 | 大小')
    for i in range(len(output_readline)):
        line = output_readline[i]
        if "]()" in line:
            line = line[1:].replace("]()", "")
        output_readline[i] = line

    # ================写入剪贴板================
    output_text = '\r\n'.join(output_readline)

    MyDef.WriteClip(output_text)
    print(MyDef.RunTime(start_time))


FileWithLink()
