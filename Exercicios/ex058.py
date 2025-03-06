#Melhore o jogo do ex028 onde o computador vai pensar em um numero entre 0 e 10
#So que agora o jogador vai tentar adivinhar ate acertar mostrando no final quantos palpites foram necessarios para vencer

import random
import time
numeroComputador = random.randint(0, 10)
contador = 0

print('-=-' * 15)
print('======JOGO DA ADIVINHACAO======')
print('-=-' * 15)
print('Ola seja bem vindo ao jogo da adivinhacao')
print('Tente acertar o numero que eu pensei')
numeroJogador = int(input('Digite um numero de 0 a 10: '))
contador = contador + 1

print('=' * 40)
while numeroJogador != numeroComputador: #While not acertou, #acertou = False
    if numeroJogador > numeroComputador:
        numeroJogador = int(input('Menos..., tente outro numero: '))
    else:
        numeroJogador = int(input('Mais..., tente outro numero: '))
    print('=' * 40)
    contador = contador + 1

time.sleep(1)
print('Parabens, Voce acertou!')
print(f'O numero escolhido era {numeroComputador}')
print(f'Voce acertou o numero em {contador} tentativas')
print('-=-' * 15)