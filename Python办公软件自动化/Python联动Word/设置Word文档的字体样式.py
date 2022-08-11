# 书写人：胡高远
# 书写时间：2022/7/20  14:42


from docx import Document
from docx.shared import Pt,RGBColor
from docx.oxml.ns import qn
doc = Document('我的文档.docx')
for para in doc.paragraphs:
    for run in para.runs:
        run.font.bold = True
        run.font.italic = True
        run.font.underline = True
        run.font.strike = True
        run.font.size = Pt(20)
        run.font.color.rgb = RGBColor(255,255,0)
        run.font.name = '微软雅黑'
        r = run._element.rPr.rFonts
        r.set(qn('w:eastAsia'),'微软雅黑')
doc.save('我的文档3.docx')

