from docx import Document

doc = Document('Joanne website.docx')
for paragraph in doc.paragraphs:
    print(paragraph.text)
