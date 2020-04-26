from googletrans import Translator
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import time
import json
import re

from selenium import webdriver
from selenium.webdriver import Firefox
import pyperclip

from docx import Document
from docx.shared import Inches

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
#pdf text data
filename=input('Enter filename:')
filename=filename + '.pdf'
text= convert_pdf_to_txt(filename)
data=text.striplines()
pattern= "[^\x20-\x7E]+"

#connect webdriver
driver = webdriver.Firefox('C:/webdriver')
url='https://deepl.com'
driver.get(url)
root=driver.find_element_by_xpath('//div [contains(@class,"lmt__language_container")]')
lang=root.find_element_by_xpath('//div [contains(@class, "lmt__language_select lmt__language_select--target")]')

lang.find_element_by_xpath('//span[contains(@class,"translate_to")]').click()

lang_menu=root.find_element_by_xpath('//div[contains(@class,"lmt__language_select__menu")]')
btn=lang_menu.find_element_by_xpath('//button[@dl-short-lang="Japanese"]')
btn.click()

trns_text=driver.find_elements_by_tag_name('textarea')

#convert pdf data
document = Document()
for d in data:
	d=re.sub(pattern, '', d)
	trns_text[0].send_keys(d)
	time.sleep(5)
	cpy_btn=driver.find_elements_by_tag_name('svg')
	cpy_btn[1].click()
	translated_data = pyperclip.paste()

	document.add_paragraph(translated_data)
	trns_text[0].clear()

document.save('Japanese.docx')
driver.close





