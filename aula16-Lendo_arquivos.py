arq = open('aula16-arquivo.txt', 'r')   #r: read
print(arq.read())
arq.close()

print()

#Outra maneira
with open('aula16-arquivo.txt', 'r') as arq2:
    print(arq2.read())
    print()
    arq2.seek(0)
    print(arq2.read())
    arq2.close()

#a=append
with open('aula16-arquivo.txt', 'a') as arq2:
    arq2.write("\nAppend")
    arq2.close()

#r+=Read & Write
with open('aula16-arquivo.txt', 'r+') as arq2:
    print()
    print(arq2.read())
    arq2.write("\nr+")
    print()
    arq2.seek(0)
    print(arq2.read())
    print("\nprint", file=arq2, end='')
    print()
    arq2.seek(0)
    print(arq2.read())
    arq2.close()

with open('Arq_criado.txt', 'w') as newarq:
    newarq.write("Novo arquivo criado")
    newarq.close()