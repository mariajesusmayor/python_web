from bs4 import BeautifulSoup
import requests
import webbrowser
import re
import os

url = "http://www.gatv.ssr.upm.es/index.php/publicaciones"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# #my approach... improved
# for divNum in range(1,16):
# 	idCont=("#toggle-id-"+str(divNum)+"-container")
# 	container = soup.select(str(idCont))
# 	for j in container:
# 		print(j.text)






#expert approach :(
idRe = 'toggle-id-\\d+-container'
texts = [x.text for x in soup.find_all(id=re.compile(idRe))]
list(map(print, texts))

print(len(texts))

os.chdir('D:\\gestores\\Web_GATV\\00_wordpress\\Version_Publicaciones')
publiFile = open('publicaciones.txt', 'w')
publiFile.write(str(texts))
publiFile.close()


