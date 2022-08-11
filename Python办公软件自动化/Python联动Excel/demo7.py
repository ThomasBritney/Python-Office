# 书写人：胡高远
# 书写时间：2022/7/14  15:07
#  输出按行的值
import openpyxl
workbook = openpyxl.load_workbook('Excel.xlsx')
sheet = workbook['产品信息']
rows = sheet.iter_rows(min_row=1,max_row=5,min_col=1,max_col=3)
for row in rows:
    for cell in row:
        print(cell.value)
    print('--------------------------')


