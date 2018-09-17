from bs4 import BeautifulSoup
import requests
import webbrowser

url = "https://www.youtube.com/watch?v=oR2CHsu5Sck"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#localizar el html del titulo
title = soup.find(id = "search")

#aislarlo
print(type(title))

print(len(title))
#mostrarlo


print(title)

#poner la URL como parametro de entrada con argv

