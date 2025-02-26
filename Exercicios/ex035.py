#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou nao formar um triangulo

lado1 = float(input('Digite o comprimento do lado1: '))
lado2 = float(input('Digite o comprimento do lado2: '))
lado3 = float(input('Digite o comprimento do lado3: '))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Pode formar um triangulo')
else:
    print('Nao pode formar um triangulo')