# 书写人：胡高远
# 书写时间：2022/7/15  14:43
import openpyxl

workbook = openpyxl.load_workbook('new project.xlsx')

sheet = workbook['Sheet1']

sheet['B8'] = '=SUM(B4:B7)'


workbook.save('new project.xlsx')
