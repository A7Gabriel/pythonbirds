

class Pessoa:
    def __init__(self,*filhos, nome = None, idade = 37):
        self.nome = nome
        self.idade = idade
        self.filhos = list()



gustavo = Pessoa(nome = 'Gustavo')
gabriel = Pessoa(gustavo,nome = 'Gabriel')
gabriel.sobrenome = 'Vieira'

del gabriel.sobrenome

print(gabriel.__dict__)




