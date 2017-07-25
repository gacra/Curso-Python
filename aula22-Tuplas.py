#Diferente das listas, as tuplas são imutáveis
#Não é possível inserir, alterar ou exculir elementos após a sua criação

tupla = ()  #Tupla vazia
tupla = (1, 2, 3, 4, 3)
print(tupla)
#Únicos métodos
print(tupla.index(4))
print(tupla.count(3))
#tupla[0] = 10 -> Erro