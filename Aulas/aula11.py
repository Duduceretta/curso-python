#Tuplas
#As TUPLAS sao IMUTAVEIS

#Tuplas sao compostas por parenteses
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
#Referncia de elementos nas tuplas
print(lanche[1]) 
#Pega o segundo elemente de tras pra frente (Pizza)
print(lanche[-2]) 
#Printa do elemente ate o elemento [3 - 1]
print(lanche[1:3])
#Printa do elemento 2 ate o final
print(lanche[2:])
#Printa do inicio ate o elemento [2 - 1]
print(lanche[:2])
#Tuplas sao imutaveis, nao e possivel fazer reatribuicao
#lanche[1] = 'Refrigerante'

#Podemos usar loops para percorre a tupla 
for comida in lanche:
    print(f'Eu vou comer {comida}')

#Outra forma, para mostrar a posicao
#for i in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[i]} na posicao {i}')

for pos, i in enumerate(lanche):
    print(f'Eu vou comer {i} na posicao {pos}')

#Ordena a tupla, mas nao altera ela
print(sorted(lanche))

#Cria uma nova tupla com os elementos das anteriores
a = (2, 5, 4)
b = (4, 7, 8, 1, 2)
#Atencao b + a é != de a + b
c = a + b 
print(c)
#Mostra quantas vezes o numero 4 aparece
print(c.count(4))
#Mostra a posicao do primeiro elemento na tupla
print(c.index(1))
#Mostra a posicao do primeiro elemento a partir de um elemento especifico
print(c.index(2, 3))
#Tuplas aceitam tipos distintos
pessoa = ('Gustavo', 39, 'M', 77.5)
#Apagar uma tupla =  del(pessoa)
print(pessoa)