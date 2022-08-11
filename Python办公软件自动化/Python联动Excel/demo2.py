# 书写人：胡高远
# 书写时间：2022/7/14  15:07
import openpyxl
workbook = openpyxl.load_workbook('Excel.xlsx')
sheet = workbook['产品信息']
cols = sheet['B']
for cell in cols:
    print(cell.value)
    print('-------------------')
