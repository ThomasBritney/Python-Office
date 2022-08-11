# 书写人：胡高远
# 书写时间：2022/7/19  15:43
from docx import Document
doc = Document('安徽教育厅办公室转发《关于做好高温天气安全生产工作的提示函》.docx')
word = input('请输入要检测的关键字：')
word_len = len(word)
count = 0
for para in doc.paragraphs:
    for i in range(0,len(para.text)-word_len+1):
        if word == para.text[i:i+word_len]:
            count+=1
print('关键字',word,'出现的次数为：',count,'次')