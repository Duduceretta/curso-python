#Faca um programa que tenha uma funcao chamada contador que receba tres parametros inicio, fim e passo e realiza a contagem
#De 1 ate 10, de 1 em 1
#De 10 ate 0, de 2 em 2
#Uma contagem personalizada

from time import sleep
from math import fabs

def contador(inicio, fim, passo):
    print('-=' * 20)
    print(f'Contagem de {inicio} ate {fim} de {int(fabs(passo))} em {int(fabs(passo))}')
    sleep(2.5)
    if passo == 0:
        passo = 1
    if inicio > fim:
        fim = fim - 1
        if passo > 0:
            passo = passo * -1
    else:
        fim = fim + 1
        if passo < 0:
            passo = passo * -1

    for i in range(inicio, fim, passo):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora e sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
