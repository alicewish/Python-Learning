def Training():
    # ======================================训练区开始======================================
    file_path_prefix = '/Users/alicewish/我的坚果云/'  # TXT文件名

    txt_file_list = ['不义联盟第五年填字001~038合并']
    info_list = []
    scenario_count_dict = {}
    scenario_list = []
    scenario_list_full = []

    # ================按行读取文本:with open(更好)================
    text_readline = []  # 初始化按行存储数据列表,不接受结尾换行符
    status_readline = []

    for txt_file_name in txt_file_list:
        txt_file_path = file_path_prefix + txt_file_name + '.txt'
        with open(txt_file_path) as fin:
            for plain_line in fin:
                plain_line = plain_line.replace('\n', '')
                plain_line = plain_line.replace('……', '…')
                if plain_line == '':
                    status = '空行'
                elif len(plain_line) == 10 and re.match(r'不义联盟第五年[0-9]{3}', plain_line):
                    status = '标题'
                elif len(plain_line) == 2 and re.match(r'[0-9]{2}', plain_line):
                    status = '页码'
                elif len(plain_line) > 12 and (plain_line[0] == '*' or plain_line[0] == '['):
                    status = '注释'
                else:
                    status = '文本'
                text_readline.append(plain_line)
                status_readline.append(status)

        # ================删除不必要信息================
        process_readline = text_readline

        for i in range(len(process_readline)):
            if status_readline[i] == '标题':
                for j in range(7):
                    process_readline[i + j] = ''
            elif status_readline[i] == '页码':
                for j in range(1):
                    process_readline[i + j] = ''
            elif status_readline[i] == '注释':
                for j in range(1):
                    process_readline[i + j] = ''

        # ================处理文本================
        empty_line_number = -1  # 初始化空行

        for i in range(0, len(process_readline)):
            if process_readline[i] == "":
                last_empty_line_number = empty_line_number  # 上一空行
                empty_line_number = i  # 这一空行
                line_number = empty_line_number - last_empty_line_number - 1  # 断行行数
                character_number_list = []  # 每行字数初始化
                character_count = 0  # 总字数初始化
                for j in range(line_number):
                    plain_line = process_readline[i - line_number + j]
                    character_number_list.append(str(len(plain_line)))
                    character_count += len(plain_line)
                store_entry = "\t".join(character_number_list)
                entry_info = [str(i), "断行行数", str(line_number), "总字数", str(character_count).zfill(2), "分配", store_entry]
                entry_info_line = "\t".join(entry_info)
                # print(entry_info_line)

                info_detail = [str(line_number)] + [str(character_count).zfill(2)] + character_number_list
                info_line = "\t".join(info_detail)
                # ================建立查询列表================
                # 总字数-断行方案
                if character_count > 0 and character_count < 70:
                    info_list.append(info_line)
                    scenario = str(character_count).zfill(2) + '\t' + store_entry
                    if scenario in scenario_list:
                        scenario_count_dict[scenario] = scenario_count_dict[scenario] + 1
                    else:
                        scenario_list.append(scenario)
                        scenario_count_dict[scenario] = 1

            else:
                pass
                # print(i, len(text_readline[a]), text_readline[a])

    all_info = "\r\n".join(info_list)
    # ================由频次排序================
    for scenario in scenario_list:
        scenario_line_list = scenario.split("\t")
        scenario_count = str(1000 - scenario_count_dict[scenario]).zfill(3)
        scenario_line_list.insert(1, scenario_count)
        scenario_line_full = '-'.join(scenario_line_list)
        scenario_list_full.append(scenario_line_full)

    scenario_list_full.sort()
    # scenario_list_full.reverse()

    print(scenario_list_full)
    # print(scenario_count_dict)
    return scenario_list_full

def Processing():
    import time, jieba, re, MyDef

    start_time = time.time()  # 初始时间戳
    scenario_list_full = Training()

    # ======================================处理区开始======================================
    dict_file_path = '/Users/alicewish/我的坚果云/userdict.txt'  # 自定义词典路径

    cut_right_count = 0
    cut_wrong_count = 0

    # ========================输入区开始========================
    input_file_path = "/Users/alicewish/Downloads/my.md"
    # ================按行读取输入文本================
    read_text = open(input_file_path, 'r').read()  # 读取文本

    text_readline = read_text.replace("\nclass", "class").replace("...", "…").splitlines()
    # print(text_readline)

    # ================按行读取文本:with open(更好)================
    status_readline = []  # 状态列表
    output_readline = []  # 输出列表

    jieba.load_userdict(dict_file_path)

    line_formmat_list_all = []

    for a in range(len(text_readline)):
        text_readline[a] = re.sub(r'<span.*</span>', '', text_readline[a])  # 去除span
        text_readline[a] = text_readline[a].replace('……', '…')

        markdown_line = text_readline[a].replace("\*", "の").replace("\[", "[").replace("\]", "]")
        print(markdown_line)
        line_cut_list = markdown_line.split("*")
        print(line_cut_list)

        plain_line = markdown_line.replace("*", "").replace("の", "*")  # 调整*
        print(plain_line)

        line_formmat_list = []

        for j in range(len(plain_line)):
            line_formmat_list.append(0)
        # print(line_formmat_list)

        line_mark_count_list = []
        for k in range(len(plain_line) + 1):
            line_mark_count_list.append(0)

        point = 0
        for char in markdown_line:
            if char == '*':
                line_mark_count_list[point] = line_mark_count_list[point] + 1
            else:
                point = point + 1
        print(line_mark_count_list)

        pin = 0
        before = 0

        for seg in line_cut_list:
            if seg == '':
                pass
            else:
                last_pin = pin
                pin += len(seg)
                # print(line_mark_count_list[last_pin])
                # print(line_mark_count_list[pin])
                if last_pin > 0:
                    before = line_formmat_list[last_pin - 1]

                for l in range(last_pin, pin):
                    if before == 0:
                        line_formmat_list[l] = before + line_mark_count_list[last_pin]
                    elif before == 1 and line_mark_count_list[last_pin] == 1:
                        line_formmat_list[l] = before - line_mark_count_list[last_pin]
                    elif before == 1 and line_mark_count_list[last_pin] == 2:
                        line_formmat_list[l] = before + line_mark_count_list[last_pin]
                    elif before == 2 and line_mark_count_list[last_pin] == 1:
                        line_formmat_list[l] = before + line_mark_count_list[last_pin]
                    elif before == 2 and line_mark_count_list[last_pin] == 2:
                        line_formmat_list[l] = before - line_mark_count_list[last_pin]
                    elif before == 3:
                        line_formmat_list[l] = before - line_mark_count_list[last_pin]
                        # print(line_formmat_list[last_pin - 1])
        print(line_formmat_list)
        line_formmat_list_all.append(line_formmat_list)

        print(plain_line)
        print(len(plain_line))

        need_cut = True  # 需要切吗?
        if len(plain_line) == 0:
            pass
        elif len(plain_line) == 2 and re.match(r'[0-9][0-9]', plain_line):
            # 页码
            need_cut = False
        elif a < 8:
            # 首部
            need_cut = False
        elif len(plain_line) > 2:
            if plain_line[0] == '*' or plain_line[0] == '[':
                # 注释
                need_cut = False

        if plain_line == "":
            status = 0  # 空行
        elif not need_cut:
            status = -1  # 不需要切
        else:
            status = 1  # 待分词
        status_readline.append(status)
        if status == 1:
            # ================结巴分词================
            string_list = []
            seg_list = jieba.cut(plain_line)  # 默认是精确模式
            for word in seg_list:
                string_list.append(word)
            print(string_list)

            start_status = False
            for i in range(len(scenario_list_full)):
                scenario_line_full = scenario_list_full[i]
                if scenario_line_full[0:2] == str(len(plain_line)).zfill(2):
                    if start_status:
                        end_i = i
                    else:
                        start_i = i
                        start_status = True
                        end_i = i
            # ================进行切分================
            current_i = start_i

            cut_right = False
            while current_i <= end_i and not cut_right:
                current_cut = scenario_list_full[current_i]
                current_cut_list = current_cut[7:].split("-")  # 列表存储的切分方案
                # ================进行分词判断================
                line_can_cut_list = []

                for i in range(len(plain_line)):
                    line_can_cut_list.append(0)

                j = 0
                for string in string_list:
                    j = j + len(string)
                    # print(j)
                    line_can_cut_list[j - 1] = 1
                # ================对标点和语气词进行纠正================
                for i in range(len(plain_line)):
                    if plain_line[i] in ',.?!，。…？！”·-》>:】【]、':
                        # 这些之前不可切
                        line_can_cut_list[i - 1] = 0
                    elif plain_line[i] in '“《<【[':
                        # 这些之后不可切
                        line_can_cut_list[i] = 0
                    elif plain_line[i] in '上中下内出完的地得了吗吧着个就前世里嘛图们来呗' and line_can_cut_list[i - 1] == 1 and line_can_cut_list[
                        i] == 1:
                        # 这些之前不可切
                        line_can_cut_list[i - 1] = 0
                    elif plain_line[i] in '太每帮跟另' and line_can_cut_list[i - 1] == 1 and line_can_cut_list[i] == 1:
                        # 这些之后不可切
                        line_can_cut_list[i] = 0
                print(line_can_cut_list)
                print(current_cut_list)

                # ================判断方案正确与否================

                sum = 0
                cut_right = True
                for i in range(len(current_cut_list)):  # 切分
                    last_sum = sum
                    sum = sum + int(current_cut_list[i])
                    print(line_can_cut_list[sum - 1])
                    print(plain_line[last_sum:sum])

                    if line_can_cut_list[sum - 1] == 0:
                        cut_right = False
                print(cut_right)
                if not cut_right:
                    current_i += 1
            if cut_right:  # 切对了
                cut_right_count += 1
                sum = 0
                for i in range(len(current_cut_list)):
                    last_sum = sum
                    sum = sum + int(current_cut_list[i])
                    output_line = plain_line[last_sum:sum]
                    output_line_format_list = line_formmat_list_all[a][last_sum:sum]
                    output_line_mark_count_list = []

                    format_list_for_use = [0] + output_line_format_list + [0]  # 11
                    for b in range(len(format_list_for_use) - 1):
                        output_line_mark_count = abs(format_list_for_use[b + 1] - format_list_for_use[b])
                        output_line_mark_count_list.append(output_line_mark_count)

                    print(output_line_mark_count_list)  # 10

                    output_markdown_line = ''

                    for c in range(len(output_line_mark_count_list) - 1):
                        for d in range(output_line_mark_count_list[c]):
                            output_markdown_line += '*'
                        output_markdown_line += output_line[c]

                    for d in range(output_line_mark_count_list[-1]):
                        output_markdown_line += '*'

                    output_readline.append(output_markdown_line)
                    print("格式", output_line_format_list)
            else:  # 切错了
                output_readline.append(text_readline[a])
                cut_wrong_count += 1
        elif status == 0:  # 不需要切
            output_readline.append('\n|\n')
        else:  # 不需要切
            output_readline.append(text_readline[a].replace("\[", "[").replace("\]", "]"))

    print('切对', cut_right_count)
    print('待切', cut_wrong_count)

    # ================写入剪贴板================
    text = '\r\n'.join(output_readline)

    MyDef.WriteClip(text)
    print(MyDef.RunTime(start_time))

Processing()