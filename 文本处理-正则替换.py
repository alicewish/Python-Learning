import re
# ================读取剪贴板================
from tkinter import Tk
r = Tk()
clipboard_content = r.clipboard_get()

replaced = re.sub('<span id=".*" class="anchor"></span>', 'a', clipboard_content)
print(replaced)