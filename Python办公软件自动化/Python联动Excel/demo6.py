# 书写人：胡高远
# 书写时间：2022/7/14  15:07
#  输出所有列的值
import openpyxl
workbook = openpyxl.load_workbook('Excel.xlsx')
sheet = workbook['产品信息']
cols = sheet.columns
for col in cols:
    for cell in col:
        print(cell.value)
        print('-------------------------')
print('cols')

