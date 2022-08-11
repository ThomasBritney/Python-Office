# 书写人：胡高远
# 书写时间：2022/7/15  14:43
import openpyxl
workbook = openpyxl.Workbook()  #创建一个新的工作簿excel文件
#创建sheet工作表
sheet = workbook.create_sheet()

sheet['A1'] = 'Hello world'

cell = sheet['A2']
cell.value = 'Python'

workbook.save('new project.xlsx')
