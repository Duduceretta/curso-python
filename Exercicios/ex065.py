#Crie um programa que leia varios numeros inteiros. No final da execucao mostre a media entre todos e qual foi o menor e maior valor lido. O programa deve perguntar ao usuario se ele quer continuar digitando mais numeros

resposta = 'S'
numero = 0
soma = 0
contador = 0
maior = -9999999
menor = 9999999

while resposta == 'S': #resposta in 'Ss'
    numero = int(input('Digite um numero: '))
    soma = soma + numero
    contador = contador + 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar digitando numeros? (S/N): ')).strip().upper()
    while resposta != 'S' and resposta != 'N':
        print('Por favor digite um caracter valido')
        resposta = str(input('Deseja continuar digitando numeros? (S/N): ')).strip().upper()

print('--' * 20)
print(f'Voce digitou {contador} numeros')
print(f'A soma total foi: {soma}')
print(f'A media total foi: {soma / contador}')
print(f'O maior valor lido foi: {maior}')
print(f'O menor valor lido foi: {menor}')
print('--' * 20)
