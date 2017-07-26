#Aspas duplas ou simples
nome = 'Guilherme'
nome = "Guilherme"

print(nome[0])
print(nome[1])
print(nome[-1])
print(len(nome))

#Strings são imitáveis
#nome[0] = 'D' -> ERRO

#Para trocar um caracter, tem que transformar em lista, trocar o caracter e transformar em string de novo

lista = list(nome)
print(lista)
lista[0] = 'D'
print(type(lista[0]))
nome = ''.join(lista)
print(nome)