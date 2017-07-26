#Nome da classe: 1ª letra de cada palavra em maiúscula

class Pessoa:

    #Construtor
    #self: próprio objeto (this)
    def __init__(self, nome):
        self.nome = nome

    def obterNome(self):
        return self.nome

    def alterarNome(self, nome):
        self.nome = nome

pessoa1 = Pessoa('Guilherme')

print(pessoa1.obterNome())
pessoa1.alterarNome('Joao')
print(pessoa1.obterNome())

pessoa2 = Pessoa('Maria')
pessoa3 = Pessoa('Guilherme')

pessoas = [pessoa1, pessoa2, pessoa3]

for p in pessoas:
    print(p.obterNome())