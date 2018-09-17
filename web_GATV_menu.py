from bs4 import BeautifulSoup
import requests
import webbrowser

url = "http://www.gatv.ssr.upm.es"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

navElem = soup.find_all(class_ = 'avia-menu-text')

urlbase = "http://www.gatv.ssr.upm.es/index.php/"

print(len(navElem))

numEnlaces =  min(3, len(navElem))

for i in range(numEnlaces):
    urldefinitiva = urlbase + navElem[i].text
    print(navElem[i].text)
    webbrowser.open(urldefinitiva)

