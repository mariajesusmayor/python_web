
from selenium import webdriver
from bs4 import BeautifulSoup
import requests


browser = webdriver.Firefox()
url = "http://www.etsit.upm.es/"
browser.get(url)

busquedaElem = browser.find_element_by_id("ke_search_sword")


texto = raw_input("¿Qué buscas? ")
busquedaElem.send_keys(texto)


busquedaElem.submit()


