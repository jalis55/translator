from selenium import webdriver
from selenium.webdriver import Firefox


driver = webdriver.Firefox('C:/webdriver')
url='https://deepl.com'
driver.get(url)
root=driver.find_element_by_xpath('//div [contains(@class,"lmt__language_container")]')
lang=root.find_element_by_xpath('//div [contains(@class, "lmt__language_select lmt__language_select--target")]')

lang.find_element_by_xpath('//span[contains(@class,"translate_to")]').click()

lang_menu=root.find_element_by_xpath('//div[contains(@class,"lmt__language_select__menu")]')
btn=lang_menu.find_element_by_xpath('//button[@dl-short-lang="Japanese"]')
btn.click()

