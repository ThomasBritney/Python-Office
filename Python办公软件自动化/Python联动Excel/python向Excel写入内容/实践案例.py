# 书写人：胡高远
# 书写时间：2022/7/15  16:22
import openpyxl
workbook = openpyxl.load_workbook('Excel.xlsx')
sheet = workbook['mysheet']
#获取所有行
rows = sheet.rows
lst = []
for row in rows:
    # print(row)
    if row[0].value == '日用品':
        sub_lst = []
        for i in range(0,3):
            sub_lst.append(row[i].value)
        lst.append(sub_lst)
print(lst)

new_workbook = openpyxl.Workbook()
new_sheet = new_workbook.active
for row in lst:
    new_sheet.append(row)

new_workbook.save('日用品信息.xlsx')
