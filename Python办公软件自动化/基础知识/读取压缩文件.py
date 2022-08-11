# 书写人：胡高远
# 书写时间：2022/7/14  9:51
import zipfile
with zipfile.ZipFile('测试文件夹1.zip', 'r') as zipobj:
    # print(zipobj.namelist())
    for file_name in zipobj.namelist():
        info = zipobj.getinfo(file_name)
        print(file_name,info.file_size,info.compress_size)