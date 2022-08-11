# 书写人：胡高远
# 书写时间：2022/7/14  14:43
import openpyxl
#  打开一个excel表格
workbook = openpyxl.load_workbook('Excel.xlsx')
print(workbook.sheetnames)

sheet = workbook['销售资料']
print(sheet.dimensions)    #获取工作表的尺寸

cell = sheet['B3']    #获取单元格
print(cell.value)

#获取一系列单元格
cells = sheet['A1:A5']
for cell in cells:
    print(cell[0].value)
    print('------------------------')
print(cells)
