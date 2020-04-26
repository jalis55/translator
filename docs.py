from docx import Document
from docx.shared import Inches

document = Document()


for i in range(10):
	document.add_paragraph("hello world")


document.save('simple.docx')