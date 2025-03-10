#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre
#Quantas vezes apareceu o valor 9
#Em que posicao foi digitado o primeiro valor 3
#Quais foram os numeros pares

tupla = tuple(int(input('Digite um numero: ')) for i in range(4))
print(f'Voce digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro numero 3 esta na {tupla.index(3) + 1}º posicao')
else:
    print(f'O numero 3 nao foi digitado')

print('Os numero pares digitados foram: ', end='')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
        