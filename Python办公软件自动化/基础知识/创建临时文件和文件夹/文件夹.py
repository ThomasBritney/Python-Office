# 书写人：胡高远
# 书写时间：2022/7/13  16:11
from tempfile import TemporaryDirectory
with TemporaryDirectory() as temp_dir:
    print(temp_dir)
    input('未结束，你可以看到文件夹')
