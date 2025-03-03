#Crie um programa que faça o computador jogar jokenpo

import random
import time

itens = ['Pedra', 'Papel', 'Tesoura']

print('-=-' * 30)
print('Ola! Vamos jogar Jokenpo?')
print('-=-' * 30)

print('Vou escolher o que eu vou jogar')
print('Pensando...')
time.sleep(1.5)
escolhaComputador = random.randint(0, 2)
print('PENSEIII!!!')
print('Agora escoolha voce: ')
print('Digite 0 se voce quer colocar pedra')
print('Digite 1 se voce quer colocar papel')
print('Digite 2 se voce quer colocar tesoura')
escolhaJogador = int(input('Qual voce escolhe?: '))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!')
print('-' * 20)
print(f'O computador escolheu {itens[escolhaComputador]}')
print(f'O jogador escolheu {itens[escolhaJogador]}')
print('-' * 20)
if escolhaComputador == 0:
    if escolhaJogador == 0:
        print('O jogo empatou vamos jogar denovo')
    elif escolhaJogador == 1:
        print('O jogador venceu')
    elif escolhaJogador == 2:
        print('O computador venceu')
    else:
        print('Opcao Invalida')
elif escolhaComputador == 1:
    if escolhaJogador == 0:
        print('O computador venceu')
    elif escolhaJogador == 1:
        print('O jogo empatou, vamos jogar denovo')
    elif escolhaJogador == 2:
        print('O jogador venceu')
    else:
        print('Opcao invalida')
elif escolhaComputador == 2:
    if escolhaJogador == 0:
        print('Jogador venceu')
    elif escolhaJogador == 1:
        print('Computador venceu')
    elif escolhaJogador == 2:
        print('O jogo empatou, vamos jogar denovo')
    else:
        print('Opcao invalida')