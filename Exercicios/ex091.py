#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario. No final coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado.

from time import sleep
from random import randint

jogadores = {}

for i in range(4):
    jogadores[f'jogador{i + 1}'] = randint(1, 6)

print('Valores Sorteados: ')
for key, value in jogadores.items():
    print(f'O {key} tirou {value} no dado'.rjust(30))
    sleep(1)

jogadoresOrdenados = dict(sorted(jogadores.items(), key=lambda x: x[1], reverse=True))

contador = 1
print('-=' * 20)
print(' == Ranking dos jogadores == ')
for key, value in jogadoresOrdenados.items():
    sleep(1)
    print(f'{contador}° lugar: {key} com {value}'.rjust(26))
    contador += 1
