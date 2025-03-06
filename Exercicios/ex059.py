#Crie um programa que leia dois valores e mostra um menu na tela
#1 - somar, 2 - multiplicar, 3 - maior, 4 - novos numeros, 5 - sair

import time

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
opcao = 0

while opcao != 5:
    print('=' * 30)
    print('O que voce deseja fazer a seguir?')
    print('[1] para somar os numeros')
    print('[2] para multiplicar os numeros')
    print('[3] para mostrar o maior valor entre os numeros digitados')
    print('[4] para digitar novos numeros')
    print('[5] para sair do programa')
    print('=' * 30)
    opcao = int(input('>>>>>> Opcao escolhida: '))

    if opcao == 1:
        print(f'A soma entre {num1} + {num2} = {num1 + num2}')
        print('Voltando para o menu...')
        time.sleep(2)
    elif opcao == 2:
        print(f'A multiplicacao entre {num1} * {num2} = {num1 * num2}')
        print('Voltando para o menu...')
        time.sleep(2)
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior valor entre {num1} e {num2} é: {num1}')
            print('Voltando para o menu...')
            time.sleep(2)
        elif num2 > num1:
            print(f'O maior valor entre {num1} e {num2} é: {num2}')
            print('Voltando para o menu...')
            time.sleep(2)
        else:
            print('Os numeros digitados sao iguais')
            print('Voltando para o menu...')
            time.sleep(2)
    elif opcao == 4:
        print('======Digitando novos numeros======')
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
        print('Numeros modificados com sucesso!')
        print('Voltando para o menu...')
        time.sleep(2)
    elif opcao == 5:
        print('Voce escolheu sair...')
    else:
        print('ERRO, Opcao nao encontrada')
        print('Por favor digite uma opcao valida')
        print('Voltando para o menu...')
        time.sleep(2)
print('Fim do Programa! Volte Sempre!')