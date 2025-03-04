#Faça um programa que leia um numero inteiro e diga se ele e ou nao um numero primo

divisores = 0
numero = int(input('Digite um numero para ver se é primo: '))

for i in range(2, numero + 1):
    if numero % i == 0:
        divisores = divisores + 1

if divisores == 1:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} nao é primo')