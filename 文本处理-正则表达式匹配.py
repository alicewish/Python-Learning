import re

test = '123'
if re.match(r'[0-9][0-9]', test):
    print('成功')
else:
    print('失败')
