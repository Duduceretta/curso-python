#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar 999 que é a condicao de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles desconsiderando a flag

numero = int(input('Digite um numero: '))
soma = 0
numerosDigitados = 0

while numero != 999:
    print('=' * 30)
    print('Digite [999] para sair')
    soma = soma + numero
    numero = int(input('Digite outro numero: '))
    numerosDigitados = numerosDigitados + 1

print(f'A soma total foi {soma}')
print(f'O total de numeros digitados foi {numerosDigitados}')
