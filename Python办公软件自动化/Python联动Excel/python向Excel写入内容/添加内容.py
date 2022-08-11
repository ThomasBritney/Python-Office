# 书写人：胡高远
# 书写时间：2022/7/15  14:43
import openpyxl
workbook = openpyxl.load_workbook('new project.xlsx')

sheet = workbook['Sheet1']

lst = ['姓名','分数']
sheet.append(lst)

stu_lst = [
    ['张三',90],
    ['李四',89],
    ['王二',78],
    ['陈六',59],
]
for row in stu_lst:
    sheet.append(row)

workbook.save('new project.xlsx')
