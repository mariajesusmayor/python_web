from bs4 import BeautifulSoup
import requests
import webbrowser
import re
import os

url = "http://www.gatv.ssr.upm.es/index.php/ofertas-de-trabajo"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

trabajos = [x.text for x in soup.find_all("div", class_="entry-content")]
list(map(print, trabajos))


#select(".slide-entry-excerpt.entry-content")
# for j in range(len(container)):
# 	print(container[j].text)


#my approach: 
# for divNum in range(1,16):
# 	idCont=("#toggle-id-"+str(divNum)+"-container")
# 	container = soup.select(str(idCont))
# 	for j in range(len(container)):
# 		print(container[j].text)


# #expert approach :(
# idRe = 'toggle-id-\\d+-container'
# texts = [x.text for x in soup.find_all(id=re.compile(idRe))]
# list(map(print, texts))
