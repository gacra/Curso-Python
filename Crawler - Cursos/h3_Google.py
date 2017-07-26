from bs4 import BeautifulSoup
import requests
import sys

url = 'https://www.google.com.br/search?q=%(q)s'
busca = {
    'q': input('>> Buscar: '),
}

print(url % busca)

r = requests.get(url % busca)
soup = BeautifulSoup(r.content.decode('latin1').encode('utf-8'), "html.parser")
titulo = [title for title in soup.find_all('h3')]
i = 0
for t in titulo:
    i+=1
    print("Título " + str(i)+ ': ' +str(t.text))

    link = t.find_next('a', href=True)
    print(link)


    #print("Link " + str(i) + ': ' + str(t.find_next('a', href=True)))
    #print("Link " + str(i) + ': ' + str(str(str(t.find_next('a', href=True)['href']).replace("/url?q=", "").rsplit("&sa=")[0])))
    #print("Resumo " + str(i)+ ': ' + str(t.find_next('span', class_='st').text))
    print()