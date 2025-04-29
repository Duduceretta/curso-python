class MinhaClasse:
    #Roda quando instanciamos um objeto
    def __init__(self, info, elem): #Metodo construtor
        self.atributi_1 = 'meu atributo'
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, 'a']
        self.atributo_novo = info
        print(self.atributo_novo)

    def metodo_1(self):
        print('Minha acao 1')
        print('Minha acao 2')
        return 'Ola mundo'
    
    def metodo_2(self, numero):
        self.metodo_1()
        print(self)

#objeto         #Classe -> instanciamos um obj
minha_classe = MinhaClasse("info aqui no construtor", 213)
minha_classe.metodo_2(3)

#response = minha_classe.metodo_1()
#print(response)
