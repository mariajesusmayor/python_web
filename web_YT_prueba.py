from bs4 import BeautifulSoup
import requests
import webbrowser

url = "https://www.youtube.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#localizar el html del titulo
title = soup.select(".div#contentContainer.style-scope.app-drawer div#guide-wrapper.style-scope.ytd-app div#guide-content.style-scope.ytd-app div#guide-inner-content.style-scope.ytd-app ytd-guide-renderer#guide-renderer.style-scope.ytd-app div#sections.style-scope.ytd-guide-renderer ytd-guide-section-renderer.style-scope.ytd-guide-renderer div#items.style-scope.ytd-guide-section-renderer ytd-guide-entry-renderer.style-scope.ytd-guide-section-renderer a#endpoint.yt-simple-endpoint.style-scope.ytd-guide-entry-renderer span.title.style-scope.ytd-guide-entry-renderer")

for i in range(len(title)):
	print(title[i].text)

print(len(title))
#aislarlo
print(type(title))

#print(len(title))
#mostrarlo


#print(title.text)

#poner la URL como parametro de entrada con argv

