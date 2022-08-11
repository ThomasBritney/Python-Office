# 书写人：胡高远
# 书写时间：2022/7/17  13:30
import openpyxl
from openpyxl.chart import LineChart,Reference
workbook = openpyxl.load_workbook('new Excel.xlsx')
sheet = workbook['薪水']

# 创建柱状图图表对象
chart = LineChart()
# 数据的应用范围
data= Reference(worksheet=sheet,min_row=2,max_row=3,min_col=1,max_col=13)
# 类别的引用范围
categories = Reference(sheet,min_row=1,max_row=2,max_col=13)
# 将数据类别添加到图表中
chart.add_data(data,from_rows=True,titles_from_data=True)
chart.set_categories(categories)
# 将图表插入到工作簿
sheet.add_chart(chart,'E8')
workbook.save('new Excel.xlsx')


# 运行有问题