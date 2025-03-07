#Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar 999, que é a condição de parada. No final mostra quantos numeros foram digitados e a soma entre eles, desconsiderando a flag

contaNumeros = 0
soma = 0

while True:
    numero = int(input('Digite um numero [999 para parar]: '))
    if numero == 999:
        break
    soma = soma + numero
    contaNumeros = contaNumeros + 1

print(f'A soma total dos {contaNumeros} foi {soma}')
print('Fim do programa')
