from lxml import html
import requests, time

start_time = time.time()  # 初始时间戳

# ========================输入区开始========================
search_term = "fake"  # 搜索的关键词
search_url = "http://youdao.com/w/eng/" + search_term  # 完整搜索网址

# ========================执行区开始========================
page = requests.get(search_url)
tree = html.fromstring(page.text)
# ====================音标====================
# nation = tree.xpath('//div[@class="baav"][1]/span/text()')  # 国别
phonogram = tree.xpath('//div[@class="baav"][1]/span[@class="pronounce"]/span/text()')  # 音标
# text = ''.join(phonogram)  # 音标文本
# phonogram_text = text.strip()  # 格式化音标文本
print("音标:\n" + phonogram[0])  # 打印格式化音标文本
# ====================释义====================
info = tree.xpath('//div[@class="trans-container"][1]//li/text()')  # 释义
text = '\r\n'.join(info)  # 释义文本
definition = text.strip()  # 格式化释义文本
print("释义:\n" + definition)  # 打印格式化释义文本

# # ====================网络释义====================
info = tree.xpath('//div[@id="webTransToggle"]//span/text()')  # 释义
text = '\r\n'.join(info)  # 释义文本
web_definition = text.strip()  # 格式化释义文本
print("网络释义:\n" + web_definition)  # 打印格式化释义文本
#
# # ====================短语====================
# info = tree.xpath('//div[@class="trans-container"][2]//li/text()')  # 释义
# text = '\r\n'.join(info)  # 释义文本
# trim_text = text.strip()  # 格式化释义文本
# print("释义:\n" + trim_text)  # 打印格式化释义文本
#
# # ====================双语例句====================
# info = tree.xpath('//div[@class="trans-container"][2]//li/text()')  # 释义
# text = '\r\n'.join(info)  # 释义文本
# trim_text = text.strip()  # 格式化释义文本
# print("释义:\n" + trim_text)  # 打印格式化释义文本

# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 两位小数的秒
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分秒取整
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
