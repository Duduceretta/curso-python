#Crie um programa que vai gerar 5 numeros aleatorios e armazenar em uma tupla
#Depois disso mostre a listagem de numeros gerados
#Indique o maior e menor valor

import random

tupla = tuple(random.randint(0, 10) for i in range(5))

for numero in  tupla:
    print(numero, end=' ')

maior = max(tupla)
menor = min(tupla)
print(f'\nO maior numero e: {maior}')
print(f'O menor numero e: {menor}')