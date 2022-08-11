# 书写人：胡高远
# 书写时间：2022/7/14  10:25
# 创建压缩包
import zipfile
file_lst = ['测试1.py','测试2.py']
with zipfile.ZipFile('压缩包.zip', 'w') as zipobj:
    for file in file_lst:
        zipobj.write(file)

# 向压缩包添加新文件
import zipfile
with zipfile.ZipFile('压缩包.zip', 'a')as zipobj:
    zipobj.write('测试3.py')