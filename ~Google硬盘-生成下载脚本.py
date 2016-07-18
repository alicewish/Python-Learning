import time, os, datetime, re, json

start_time = time.time()  # 初始时间戳

# documentId = "1bB3RGo1tHFTnYgQ9M56d42AtYq9x3fLYVBR4qHdmrzY"
# documentName = "sample.docx"


a = """
    var documentId = "
"""
b = """
"
    var forDriveScope = DriveApp.getStorageUsed(); //needed to get Drive Scope requested
    var url = "https://docs.google.com/feeds/download/documents/export/Export?id=" + documentId + "&exportFormat=docx";
    var param = {
        method: "get",
        headers: {"Authorization": "Bearer " + ScriptApp.getOAuthToken()},
        muteHttpExceptions: true,
    };
    var html = UrlFetchApp.fetch(url, param).getContentText();
    var file = DriveApp.createFile("
"""

c = """
", docx);
    file.getUrl();
"""

script_list = ["function runThis() {"]
# ================读取剪贴板================
from tkinter import Tk

r = Tk()
read_text = r.clipboard_get()
text_readline = read_text.splitlines()  # 对数据分行
print(text_readline)
for i in range(len(text_readline)):
    if "\t" in text_readline[i]:  # 接受key value格式
        split_line = text_readline[i].split("\t")
        documentName = split_line[0].zfill(2)
        documentId = split_line[1]
        script_entry = a.strip("\n") + documentId + b.strip("\n") + documentName + c.strip("\n")
        script_list.append(script_entry)
script_list.append("}")
text = "\r\n".join(script_list)
print(text)
# ================写入剪贴板================
import pyperclip

pyperclip.copy(text)
spam = pyperclip.paste()
# ================运行时间计时================
run_time = time.time() - start_time
if run_time < 60:  # 秒(两位小数)
    print("耗时:{:.2f}秒".format(run_time))
elif run_time < 3600:  # 分+秒(取整)
    print("耗时:{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60))
else:  # 时分秒取整
    print("耗时:{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60))
