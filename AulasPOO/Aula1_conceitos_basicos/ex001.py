#Crie uma classe Pessoa com os atributos altura e idade e com metodos comer e correr

class Pessoa:
    def __init__(self, nome, altura, idade):
        self.nome = nome
        self.altura = altura
        self.idade = idade

    def comer(self):
        print(f'A pessoa {self.nome} esta comendo!')

    def correr(self):
        print(f'A pessoa {self.nome} saiu para correr...')


pessoa1 = Pessoa('Eduardo', 1.75, 20)
pessoa1.comer()
pessoa1.correr()