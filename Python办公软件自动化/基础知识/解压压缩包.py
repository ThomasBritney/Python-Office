# 书写人：胡高远
# 书写时间：2022/7/14  10:00
import zipfile
with zipfile.ZipFile('测试文件夹1.zip', 'r') as zipobj:
    zipobj.extractall('D:/new_file')