#Hash do Python
#{chave:valor}
#Não garante ordem

d = {'Marcos':28, 'Guilherme':25, 'Maria':40}

print(d['Marcos'])
print(d['Maria'])

print(d.keys())
print(d.values())
print(d)

del d['Marcos']
print(d)

print('Marcos' in d)
print('Maria' in d)