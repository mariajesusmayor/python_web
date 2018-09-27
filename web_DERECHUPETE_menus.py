# -*- coding: utf-8 -*-

import bs4
import requests
import re
import sys
import pyperclip


if len(sys.argv) > 1:

	URL = " ". join(sys.argv[1:])

else:
	URL = pyperclip.paste()

res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

nombreReceta = soup.find("h1")
print(nombreReceta.text)

rankingReceta = soup.find(class_="rating_score")
print(rankingReceta.text)

detalles = [detalle.text for detalle in soup.find_all(id="extrainfo")]
list(map(print, detalles))

ingredientes = [ingrediente.text for ingrediente in soup.find_all(id="ingredients")]
list(map(print, ingredientes))


#no discrimina entre el menú de navegación y el lateral.
##idRe = "menu-item-\\d+"
##elemNav = soup.find_all(id=re.compile(idRe))
##for elem in elemNav:
##	print(elem.text)





