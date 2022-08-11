# 书写人：胡高远
# 书写时间：2022/7/16  15:46
import openpyxl
from openpyxl.styles import Side,Border
workbook = openpyxl.load_workbook('project.xlsx')
sheet = workbook['Sheet1']
cell = sheet['A1']
side = Side(style='thin',color='ff0000')
border = Border(left=side,top=side,right=side,bottom=side)
cell.border = border
workbook.save('project.xlsx')
