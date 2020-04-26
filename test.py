from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
import re

def pdf_to_text(path):
	manager = PDFResourceManager()
	retstr = BytesIO()
	layout = LAParams(all_texts=True)
	device = TextConverter(manager, retstr, laparams=layout)
	filepath = open(path, 'rb')
	interpreter = PDFPageInterpreter(manager, device)
	for page in PDFPage.get_pages(filepath, check_extractable=True):
		interpreter.process_page(page)
	text = retstr.getvalue()
	filepath.close()
	device.close()
	retstr.close()
	#return text
	return text.decode('ascii', errors='ignore')

if __name__ == "__main__":
	text = pdf_to_text("C:/Users/jalis/Desktop/pdf to japaness/trust me im lying.pdf")
	# pattern= "[^\x20-\x7E]+"
	# text=str(text)
	# text=re.sub(pattern,'',text)
	f=open('output2.txt','w')
	f.write(text)