# 书写人：胡高远
# 书写时间：2022/7/14  15:07
#  输出按列的值
import openpyxl
workbook = openpyxl.load_workbook('Excel.xlsx')
sheet = workbook['销售资料']
cols = sheet['E']  #获取c列
count = 0
for col in cols:
    if col.value == '美国':
        count+=1
        print('E'+str(col.row))
print('销往美国',count,'种类商品')

