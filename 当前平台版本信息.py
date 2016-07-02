import platform, sys, os

print(platform.python_version())
print(sys.version)
print(sys.version_info)
print(os.getcwd())
print(sys.getdefaultencoding())
print(os.name)
print(os.uname())  # 详细的系统信息
print(os.environ)  # 在操作系统中定义的环境变量，全部保存在os.environ这个dict中


