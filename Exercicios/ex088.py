#Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo. Cadastrando tudo em uma lista composta

from time import sleep
import random

i = 0
numeroPalpites = int(input('Quantos palpites voce quer gerar?: '))
guardaJogo = []

print('--' * 20)
print(f'{"JOGO DA MEGA SENA":^40}')
print('--' * 20)
print(f'SORTENADO {numeroPalpites} JOGOS')
while i < numeroPalpites:
    lista = random.sample(range(1, 60), 6)
    lista.sort()
    guardaJogo.append(lista)
    i = i + 1

for pos, k in enumerate(guardaJogo):
    print(f'Jogo {pos + 1} = {k}')
    sleep(1)    
