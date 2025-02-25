#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hypotenusa
import math

cateto1 = float(input('Digite o cateto1: '))
cateto2 = float(input('Digite o cateto2: '))
print(f'A hipotenusa é: {math.hypot(cateto1, cateto2):.2f}')
