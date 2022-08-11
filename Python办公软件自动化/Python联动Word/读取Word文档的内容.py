# 书写人：胡高远
# 书写时间：2022/7/19  15:24
from docx import Document
# 读取Document
doc = Document('我的文档.docx')
paras = doc.paragraphs    #获取的是段落的列表
# print(paras)
for item in paras:
    runs = item.runs
    for run in runs:
        print(run.text)
    print('---------------')
