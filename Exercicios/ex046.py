#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio indo de 10 ate 0, com uma pausa de 1 segundo entre eles

import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)
print('KABOOMMMMMM')