# 书写人：胡高远
# 书写时间：2022/7/20  15:16
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt

doc = Document('我的文档.docx')
for para in doc.paragraphs:
    para.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    #两倍行间距
    para.paragraph_format.line_spacing = 2.0
    #段前段后间距
    para.paragraph_format.space_before = Pt(20)
    para.paragraph_format.space_after = Pt(30)





doc.save('我的文档4.docx')

