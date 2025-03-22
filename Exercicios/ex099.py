#Faca um programa que tenha uma funcao chamada maior que receba varios parametros com valores inteiros.
#Seu programa tem que analisar todos valores e dizer qual e o maior

from time import sleep


def maior(*numeros):
    print('-=' * 30)
    print('Analisando os valores passados...')
    maior = 0
    for i in range(0, len(numeros)):
        print(numeros[i], end=' ', flush=True)
        sleep(0.5)
        if i == 0:
            maior = numeros[0]
        else:
            if numeros[i] > maior:
                maior = numeros[i]
    print(f'Foram informados {len(numeros)} valores ao todo')
    print(f'O maior numero passado foi: {maior}')


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
