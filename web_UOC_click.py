from selenium import webdriver
import requests

browser = webdriver.Firefox()
url = "http://www.uoc.edu"
browser.get(url)

navElem = browser.find_elements_by_class_name("col-sm-offset-1")
print(len(navElem))


tagElem = browser.find_elements_by_class_name("w100-inline-block.ruler.ruler--ri")

#tagElem = browser.find_elements_by_class_name("brand-text")



print(len(tagElem))
print(type(tagElem))
print(tagElem)




#or i in range(len(tagElem)):
    #print("Elemento " + str(i) + " " + str(tagElem[i]))
    #print(tagElem.getText())

#divElem = browser.find_element_by_class_name("col-xs-12.col-clear.page-module.nav-brands-desktop")
