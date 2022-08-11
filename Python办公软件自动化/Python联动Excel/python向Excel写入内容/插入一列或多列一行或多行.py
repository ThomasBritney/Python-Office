# 书写人：胡高远
# 书写时间：2022/7/15  15:33
import openpyxl
workbook = openpyxl.load_workbook('new project.xlsx')
sheet = workbook['Sheet1']

# sheet.insert_cols(idx=1)  #插入一列

# sheet.insert_cols(idx=2,amount=3)    #插入多列

# sheet.insert_rows(idx=2)    # 插入一行

# sheet.insert_rows(idx=4,amount=3)   #插入多行

# sheet.delete_cols(idx=1,amount=4)   # 删除多行

# sheet.delete_rows(idx=2,amount=5)


sheet.move_range('A2:B7',rows=3,cols=2)   #移动格子


workbook.save('new project.xlsx')