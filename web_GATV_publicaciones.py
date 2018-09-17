from bs4 import BeautifulSoup
import requests
import webbrowser

url = "http://www.gatv.ssr.upm.es/index.php/publicaciones/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

aniosPub = soup.find_all(class_ = 'toggler') #contenedor en el que está el año

for i in range(len(aniosPub)):
    print("Esta publicación corresponde al año " + (aniosPub[i].text))
    
print(len(aniosPub))  #15elementos, uno por año de existencia del grupo.

print(aniosPub[14]) #contenido de p.class="toggler"
print(type(aniosPub))
print(type(aniosPub[14]))


#print(type(aniosPub))

#print(aniosPub[0].text)


#print("objeto find all " + str(type(aniosPub)))

#aniosPub_cadena = str(aniosPub)

#print(aniosPub_cadena)

tipoPub = soup.select("h4") #contenedor en el que está cada tipo de publicación
print("esto es el tipo de un rótulo " + str(type(tipoPub)))



print(tipoPub)
print("tipo publicación, primer elemento: " + tipoPub[0].text)
print(len(tipoPub))

for i in range(len(tipoPub)):
    print("este es el rótulo número " + str(i) + " " + tipoPub[i].text)

#noticias = soup.find_all(class_ = "news_link")

#print(noticias)
