#Todos os atributos ou metodos que nao comecarem com '__' sao publicos
#Metodos e atributos privados so podem ser acessados dentro da propria classe

class Pessoa:
    def __init__(self, altura, cpf):
        self.altura = altura
        #atributo privado '__'
        self.__cpf = cpf

    def apresentar(self):
        print(f'Ola, minha altura - {self.altura}')
        #consegue acessar o metodo pois esta na mesma classe
        self.__coletar_documento()

    #metodo privado comeca com '__'
    def __coletar_documento(self):
        print(f'Meu documento - {self.__cpf}')


jorge = Pessoa('1,70', '74386228')
jorge.apresentar()

# Nao acessa pois e privado
#jorge.__coletar_documento()