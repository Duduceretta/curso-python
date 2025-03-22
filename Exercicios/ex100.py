#Faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteio e somaPar. A primeira vai sortear 5 numeros e adicionalos dentro da lista. E a segunda funcao vai mostrar a soma entre todos os valores pares sorteados pela funcao anterior

from random import randint
from time import sleep


def sorteio(lst):
    print('Sorteando 5 valores para a lista: ', end='')
    for i in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[i], end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lst2):
    soma = 0
    print(f'Somando os valores pares de {lst2}, temos ', end='')
    for i in range(0, len(lst2)):
        if lst2[i] % 2 == 0:
            soma += lst2[i]
    print(soma)


#Programa principal
listaNumeros = []
sorteio(listaNumeros)
somaPar(listaNumeros)
