
from googletrans import Translator
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import time
import json
import re

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()


    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)


    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


start_time = time.time()
text= convert_pdf_to_txt('assignment1.pdf')
data=[]
n=100
pattern= "[^\x20-\x7E]+"
for i in range(0, len(text), n):
    data.append("".join(text[i:i+n]))



f=open('japanese.txt','w')
for d in data:
	d=re.sub(pattern, '', d)
	f.write(d+'\n')


print("--- %s seconds ---" % (time.time() - start_time))