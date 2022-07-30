



class Motor:
    def __init__(self):
        self.velocidade = 1

    def acelerar(self):
        self.velocidade += 1
        print(f'O carro está {self.velocidade} por hora')

    def frear(self):
        self.velocidade -= 1
        if self.velocidade >=1:
            print(f'O carro está {self.velocidade} por hora')
        else:
            print(f'O carro já está parado!')
            self.velocidade = 0
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao():
    rotacao_a_direita_dict = {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE}
    rotacao_a_esquerda_dict = {NORTE:OESTE,OESTE:SUL,SUL:LESTE,LESTE:NORTE}
    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]
        print(f'À direita, o carro está indo em direção: {self.valor}')

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]


        print(f'À esquerda, o carro está indo em direção: {self.valor}')


