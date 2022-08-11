# 书写人：胡高远
# 书写时间：2022/7/15  16:00
import openpyxl
workbook = openpyxl.load_workbook('Excel.xlsx')


# sheet = workbook['mysheet']
# sheet.freeze_panes = 'A2'

sheet = workbook['mysheet']
sheet.auto_filter.ref = sheet.dimensions

workbook.save('Excel.xlsx')


