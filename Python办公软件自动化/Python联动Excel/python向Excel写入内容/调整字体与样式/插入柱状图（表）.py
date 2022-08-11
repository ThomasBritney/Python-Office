# 书写人：胡高远
# 书写时间：2022/7/17  13:30
import openpyxl
from openpyxl.chart import BarChart,Reference
workbook = openpyxl.load_workbook('new Excel.xlsx')
sheet = workbook['产品销售情况']

# 创建柱状图图表对象
chart = BarChart()
# 数据的应用范围
data = Reference(worksheet=sheet,min_row=1,max_row=117,min_col=1,max_col=2)
# 类别的引用范围
categories = Reference(sheet,min_row=2,max_row=117,min_col=1)
# 将数据类别添加到图表中
chart.add_data(data,titles_from_data=True)
chart.set_categories(categories)
# 将图表插入到工作簿
sheet.add_chart(chart,'D4')
workbook.save('new Excel.xlsx')