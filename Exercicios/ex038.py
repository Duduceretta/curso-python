#Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela
#O primeiro valor e maior
#O segundo valor e maior
#Os dois sao iguais

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'O numero {num1} e maior que {num2}')
elif num2 > num1:
    print(f'O numero {num2} e maior que {num1}')
else:
    print(f'Os dois numeros sao iguais')
    