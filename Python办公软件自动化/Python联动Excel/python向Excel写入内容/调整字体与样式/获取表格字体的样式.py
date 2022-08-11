# 书写人：胡高远
# 书写时间：2022/7/16  15:33
import openpyxl
from openpyxl.styles import Font
workbook = openpyxl.load_workbook('../new project.xlsx')
sheet = workbook['Sheet1']
cell = sheet['A1']
font = cell.font
print(font.name,font.size,font.bold,font.color)
