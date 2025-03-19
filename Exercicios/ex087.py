#Aprimore o desafio anterior, mostrando no final
#A soma de todos os valores pares
#A soma dos valores da terceira coluna
#O maior valor da segunda linha

matriz = [[0] * 3 for i in range(3)]
somaPares = 0
somaTerceiraColuna = 0

for i in range(3):
    for j in range(3):
        numero = int(input(f'Digite um numero para a posicao {i, j}: '))
        matriz[i][j] = numero

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            somaPares = somaPares + matriz[i][j]
        if j == 2:
            somaTerceiraColuna = somaTerceiraColuna + matriz[i][j] 
    print()

maiorSegundaLinha = matriz[1][0]
for i in matriz[1]:
    if i > maiorSegundaLinha:
        maiorSegundaLinha = i
    
print(f'A soma total dos numeros pares da matriz e: {somaPares}')
print(f'A soma total da terceira coluna da matriz e: {somaTerceiraColuna}')
print(f'O maior valor da segunda linha e: {maiorSegundaLinha}')
