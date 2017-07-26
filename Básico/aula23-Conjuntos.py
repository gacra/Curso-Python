#Conjuntos ou sets
#Estrutura de dados não ordenada (não são armazenados na ordem de inserção) sem elementos repetidos

c = {2, 2, 2, 'Marcos', 'Marcos'}
print(c)            
print(len(c)) #len funciona para td (listas, tuplas, conjuntos, strings, etc)

lista = [1, 1, 1, 2, 2, 2, 3, 3]
print(lista)
c = set(lista)
print(c)
c.add(2)    #Não terá efeito, pois já tem 2 no conjunto
print(c)
c.add('Guilherme')
print(c)
c.remove('Guilherme')
print(c)