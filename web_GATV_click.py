from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import requests

browser = webdriver.Firefox()
url = "http://www.gatv.ssr.upm.es"
browser.get(url)

#tagElem = browser.find_elements_by_class_name("entry-content-header")

wait = WebDriverWait(browser,5)

for tagElem in browser.find_elements_by_class_name("avia-menu-text"):
	if tagElem.text == "":
		print("Sin texto")
	else:
		print("ejecutando el bucle: " + tagElem.text)

print(type(tagElem))
print(tagElem)

#print(tagElem[0])


#or i in range(len(tagElem)):
    #print("Elemento " + str(i) + " " + str(tagElem[i]))
    #print(tagElem.getText())

#divElem = browser.find_element_by_class_name("col-xs-12.col-clear.page-module.nav-brands-desktop")
