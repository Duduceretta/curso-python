#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, coseno e tangente desse ângulo
import math

angulo = math.radians(int(input('Digite um angulo em graus: ')))
print(f'O seno de {math.degrees(angulo):.2f} é: {math.sin(angulo):.2f}')
print(f'O cosseno de {math.degrees(angulo):.2f} é: {math.cos(angulo):.2f}')
print(f'A tangente de {math.degrees(angulo):.2f} é: {math.tan(angulo):.2f}')
