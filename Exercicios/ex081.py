#Crie um programa que vai ler varios numeros e colocar em uma lista, depois disso mostre
#Quantos numeros foram digitados
#A lista ordenada de forma decrescente
#Se o numero 5 foi digitado e esta ou nao na lista
import time
cont = 0
lista = []

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    cont += 1
    reposta = str(input('Deseja continuar? (S/N): ')).upper().strip()
    while reposta not in 'SN':
        reposta = str(input('Comando invalido. Deseja continuar? (S/N): ')).upper().strip()
    
    if reposta == 'N':
        print('Saindo do programa...')
        time.sleep(1)
        break

listaDescrescente = lista.copy()
listaDescrescente.sort(reverse=True)

print(f'Foram digitados {cont} numeros')
print('Lista em ordem decrescente: ', end='')
print(listaDescrescente)
if 5 in lista:
    print('O numero 5 faz parte da lista!')
else:
    print('O numero 5 nao faz parte da lista!')