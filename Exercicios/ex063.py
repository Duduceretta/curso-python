#Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci

numero = int(input('Digite quantos elementos da sequencia de fibonacci voce quer ver: '))

primeiro = 0
segundo = 1

print(f'{primeiro} -> {segundo}', end=' -> ')
while numero > 2:
    proximo = primeiro + segundo
    print(f'{proximo}', end=' -> ')
    primeiro = segundo
    segundo = proximo
    numero = numero - 1

print('ACABOU')
