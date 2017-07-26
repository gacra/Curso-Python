#Aula 19

lista = [1, 2, 3, 4]
print(lista)    #No IDLE não precisa do print
lista = [1, 2, "Guilherme", "Luke", 3.14, 2.155]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[4])
print(lista[5])
print()

#Aula20

lista = [1, 'Guilherme', 3.14]
print(lista)
lista.append('joao')
print(lista)
print(lista[-1]) #Último elemento
print(len(lista)) #Tamanho da lista

lista2 = [2, 3, 4]
lista.extend(lista2)
print(lista)

lista.insert(0, 'Maria')
print(lista)
lista.insert(2, 'Luke')
print(lista)
print()

#Aula 21

lista = []  #Criar listas vazias
lista.extend([1, 2, 3, 4, 'Guilherme'])
print(lista)
lista.remove(3) #Remove passando o elemento
print(lista)
lista.remove('Guilherme')
#lista.remove('joao') ->Remover elementos que não estão na lista dá erro
print(lista)
lista.pop(1)    #Remove passando o índice
print(lista)
lista.clear()
print(lista)

lista = ['Marcos', 'Python', 10, 'Python']
print(lista.index('Marcos'))
print(lista.index('Python'))    #Retorna a primeira vez que aparece
print(lista.count('Python'))    #Conta quantas vezes aparece
lista.remove('Python')  #Remove somenta a primeira ocorrencia
print(lista)

lista = [10, 1, 3.8, 7.87]
lista.sort()
print(lista)                        

lista = ['Maria', 'Ana', 'Pedro']
lista.sort(reverse = True)
print(lista)
print()

#Aula 20 - Início

lista = [1, 2, 3]
lista[0] = 10
print(lista)

if 2 in lista:
    print('Esta')
else:
    print('Nao esta')