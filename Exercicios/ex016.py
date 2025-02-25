#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira Ex: 6.127 = 6 
import math

numero = float(input("Digite um numero qualquer: "))
print(f'A parte inteira do numero {numero} é: {math.trunc(numero)}')