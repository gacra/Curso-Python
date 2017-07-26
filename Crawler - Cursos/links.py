from bs4 import BeautifulSoup
import requests
import sys

def buscar_links(url):
    if 'http' not in url:
        url = 'http://' + url
    lista = []
    i = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    for a in soup.find_all('a', href=True):
        link = a['href']
        #links = str(link).strip('[]').replace("u", "").replace("'", "")
        i += 1
        lista.append(link)
        print(link)

url = 'https://www.google.com.br/search?q=%(q)s'
busca = {
    'q': input('>> Buscar: '),
}

buscar_links(url % busca)
