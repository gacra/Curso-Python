#http://zeldani.blogspot.com.br/2012/11/criando-um-webcrawler-em-python.html

from bs4 import BeautifulSoup
import requests
import sys

url = 'http://www.youtube.com/results?search_query=%(q)s'
busca = {
    'q': input('>> Buscar: '),
}

print(url % busca)

r = requests.get(url % busca)
soup = BeautifulSoup(r.content, "html.parser")
titulo = [title.text for title in soup.find_all('h3')]
i = 0
for t in titulo:
    i+=1
    print(str(i)+ ' ' +str(t))