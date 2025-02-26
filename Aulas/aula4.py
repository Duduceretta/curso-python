#Manipulacao de texto
frase = 'Curso em Video Python'
#Fatiamento 
#Pega o indice 9 = V
print(frase[9])
#Pega a palavra Vide, porque ele exclui a ultima posicao = 13 = letra 'o'
print(frase[9:13])
#Vai de 9 ate 21 pulando de 2 em 2
print(frase[9:21:2])
#Vai do inicio ate o 4 = 5 -1
print(frase[:5])
#Vai do 15 ate o final da string
print(frase[15:])
#Vai do 9 ate o fim pulando de 3 em 3
print(frase[9::3])

#Análise
#Comprimento da String
print(len(frase))
#Conta quantas letras 'o' tem na frase, com fatiamento
print(frase.count('o',0,13))
#Indica a primeira posicao onde ele encontrou 'deo'
print(frase.find('deo'))
#Indica a ultima ocorrencia da letra 'a'
frase.rfind('a')
#Verifica se a palavra 'Curso' existe na frase
print('Curso' in frase)

#Transformacao
#Troca a palavra Python por Android
frase.replace('Python', 'Android')
#Bota a frase toda em Maiuscula
frase.upper()
#Bota a frase toda em Minuscula
frase.lower()
#Todas as letras Minusculas, menos a letra inicial que fica maiuscula
frase.capitalize()
#Bota todo inicio de palavra com letra maiuscula
frase.title()
#Remove os espaços no fim e inicio da frase
frase.strip()
#Remove os espaços da direita
frase.rstrip()
#Remove os espaços da esquerda
frase.lstrip()

#Divisao
#Gera uma lista com cada palavra dividida por espaços
frase.split()

#Juncao
#Juntaria todas as palavras separando por '-'
'-'.join(frase)