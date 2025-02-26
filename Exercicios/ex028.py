#Escreva um programa que faça o computador pensar em um numero entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido. O programa devera escrever se o usuario ganhou ou perdeu
import emoji
import random
import time 

numeroPensado = random.randint(0,5)
print('Estou pensando em um numero...')
time.sleep(1)
print(emoji.emojize('PENSEI' ":bulb:" '!!', language="alias"))
print('Tente adivinhar o meu numero!!')
numeroUsuario = int(input('Digite um numero de 0 a 5: '))
if numeroUsuario == numeroPensado:
    print('Parabens, voce acertou o numero!!')
    print(f'O numero era {numeroPensado}')
else:
    print(f'OH nao, voce errou, o numero era {numeroPensado}')