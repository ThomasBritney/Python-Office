# 书写人：胡高远
# 书写时间：2022/7/13  16:01
from tempfile import TemporaryFile
file=TemporaryFile('w+')
file.write('老师好')
file.seek(0)
print(file.readlines())
print(file.name)
input('先别结束，查看文件是否存在')
file.close()
print('----------------------------')
#推荐使用的写法with...as
with TemporaryFile('w+') as file:
    file.write('老师好啊')
    file.seek(0)
    print(file.readlines())
