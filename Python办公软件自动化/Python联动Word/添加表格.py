# 书写人：胡高远
# 书写时间：2022/7/19  16:25
from docx import Document
doc = Document()
'''准备表格中的数据'''
lst = [
    ['学号','姓名','成绩'],
    [101,'张三',97],
    [102,'李四',88],
    [103,'王二',100]
]

table = doc.add_table(rows = 4,cols = 3)
for index in range(4):
    cells = table.rows[index].cells  #获取行中的单元格
    for idx in range(3):
        cells[idx].text = str(lst[index][idx])

# 保持文档
doc.save('表格.docx')