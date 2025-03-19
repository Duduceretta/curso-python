#Crie um programa que cria uma matriz 3x3 e preencha com valores lidos pelo teclado
#No final mostre na tela com a formatacao correta

#Minha solucao
'''matriz = [[],[],[]]

for i in range(0, 3):
    for j in range(0, 3):
        numero = int(input(f'Digite um numero para a posicao {i,j}: '))
        matriz[i].append(numero)

for i in range(0, 3):   
    print(f'{matriz[i]}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um numero para a posicao {i , j}: '))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()
