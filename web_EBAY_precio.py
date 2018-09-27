# -*- coding: utf-8 -*-


import bs4
import requests

URL = "https://www.ebay.com/itm/For-Macbook-Air-Pro-Retina-11-12-13-Rubberized-Hard-Keyboard-Protector-Cover/112462162960?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20180518101550%26meid%3D6d73b8d1898e49c898de1e711de23add%26pid%3D100970%26rk%3D1%26rkt%3D1%26mehot%3Dag%26sd%3D112462162960%26itm%3D112462162960&_trksid=p2481888.c100970.m5481&_trkparms=pageci%3Aac148781-beb3-11e8-a0d7-74dbd18073aa%7Cparentrq%3A035151dc1660aa66b44ae0c6fffba21d%7Ciid%3A1"

res = requests.get(URL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")


article = soup.find(class_="it-ttl")
print(article.text)

price = soup.find(class_="notranslate")
print(price.text)

sold =soup.find(class_="w2b-sgl")
print(sold.text)

# Realizamos la petición a la web







