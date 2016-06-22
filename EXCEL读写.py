import time, xlrd, xlwt

start_time = time.time()  # 初始时间戳

file_path = '/Users/alicewish/我的坚果云/Excel_Workbook.xls'

# 读取EXCEL
data = xlrd.open_workbook(file_path)  # 打开Excel文件读取数据  # 获取一个工作表

table = data.sheets()[0]  # 通过索引顺序获取
print(table)
table = data.sheet_by_index(0)  # 通过索引顺序获取
print(table)
table = data.sheet_by_name(u'My Worksheet')  # 通过名称获取
print(table)
# 获取整行和整列的值（返回数组）
table.row_values(0)
print(table.row_values(0))
table.col_values(0)
print(table.col_values(0))

# 获取行数和列数
table.nrows
print(table.nrows)
table.ncols
print(table.ncols)
# 获取单元格
table.cell(0, 0).value
print(table.cell(0, 0).value)
table.cell(0, 1).value
print(table.cell(0, 1).value)
table.cell(1, 0).value
print(table.cell(1, 0).value)
table.cell(1, 1).value
print(table.cell(1, 1).value)

# 写入EXCEL

workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook
worksheet = workbook.add_sheet('My Worksheet')  # 创建表
worksheet.write(0, 0, label='Row 0, Column 0 Value')  # 往单元格内写入内容
worksheet.write(0, 1, label='Row 0, Column 1 Value')  # 往单元格内写入内容
worksheet.write(1, 0, label='Row 1, Column 0 Value')  # 往单元格内写入内容
worksheet.write(1, 1, label='Row 1, Column 1 Value')  # 往单元格内写入内容

workbook.save(file_path)  # 保存

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
