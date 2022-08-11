# 书写人：胡高远
# 书写时间：2022/7/16  15:36
import openpyxl
from openpyxl.styles import Alignment
workbook = openpyxl.load_workbook('../new project.xlsx')
sheet = workbook['Sheet1']
cell = sheet['A1']
algin = Alignment(horizontal='center',vertical='center')
cell.alignment = algin
workbook.save('project.xlsx')
