# 书写人：胡高远
# 书写时间：2022/7/16  16:05
import openpyxl

workbook = openpyxl.load_workbook('project.xlsx')
sheet = workbook['Sheet1']

sheet.row_dimensions[2].height = 50
sheet.column_dimensions['B'].width = 20
workbook.save('project.xlsx')
