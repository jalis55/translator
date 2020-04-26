from selenium import webdriver
from selenium.webdriver import Firefox
import pyperclip

import time


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
trns_text[0].send_keys("Hi I am Jalis Mahamud Tarif who is developing a python scripts")
time.sleep(20)
cpy_btn=driver.find_elements_by_tag_name('svg')
cpy_btn[1].click()

s = pyperclip.paste()
print(s)

trns_text[0].clear()

