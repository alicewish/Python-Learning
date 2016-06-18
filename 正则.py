import requests, html2text, re

html = requests.get('http://sinacn.weibodangan.com//user/1788862154/')  # 代抓
p = re.compile(r'\d{3,}')  # 正则抓三位以上数字
num = p.findall(html2text.html2text(html.text))  # 查找全部
print('\n' + "数字ID " + num[2] + '\n' + '关注Following ' + num[4] + '\n' + '粉丝Fans ' + num[5] + '\n' + '微博Posts ' + num[6])
f = open('/Users/alicewish/我的坚果云/Python.txt', 'w')
long = "数字ID " + num[2] + '\n' + '关注Following ' + num[4] + '\n' + '粉丝Fans ' + num[5] + '\n' + '微博Posts ' + num[6]
try:
    f.write(long)
finally:
    f.close()
