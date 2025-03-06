#Faça um programa que leia um numero qualquer e mostre o seu fatorial

numero = int(input('Digite um numero para saber seu fatorial: '))
numeroAuxiliar = numero
fatorial = 1
print(f'Calculando {numero}! = ', end='')
while numero > 0:
    print(f'{numero}', end='')
    print(' x ' if numero > 1 else ' = ', end= '')
    fatorial = fatorial * numero
    numero = numero - 1
    
print(f'{fatorial}')
