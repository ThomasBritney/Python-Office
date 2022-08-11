# 书写人：胡高远
# 书写时间：2022/7/14  15:07
#  输出所有行的值
import openpyxl
workbook = openpyxl.load_workbook('Excel.xlsx')
sheet = workbook['产品信息']
rows = sheet.rows
for row in rows:
    for cell in row:
        print(cell.value)
    print('-----------------------------')

