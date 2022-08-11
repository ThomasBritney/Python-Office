# 书写人：胡高远
# 书写时间：2022/7/16  15:20
#  修改字体样式
import openpyxl
from openpyxl.styles import Font
workbook = openpyxl.load_workbook('../new project.xlsx')
sheet = workbook['Sheet1']
cell = sheet['A1']
font = Font(name='微软雅黑',size=20,bold=True,italic=True,color='ff0000')
cell.font = font
workbook.save('new project.xlsx')

