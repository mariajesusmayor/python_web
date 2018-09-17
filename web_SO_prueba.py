from bs4 import BeautifulSoup
import requests
import webbrowser

url = "https://stackoverflow.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#topquestions
title = soup.select("h1.grid--cell")

#mostrarlo
print(title[0].text.strip())

#recuperar las n primeras y dar el enunciado de la pregunta

