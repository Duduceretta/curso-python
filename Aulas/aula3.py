#Utilizando modulos
#Importa um comando especifico da biblioteca math
#from math import sqrt
#importa toda a biblioteca math e a biblioteca random
import math
import random
import emoji
#math.floor(raiz) arredonda o num para baixo

num = int(input('Digite um numero: '))
raizQuadrada = math.sqrt(num)
print(f'A raiz de {num} é: {raizQuadrada:.2f}')

numeroAleatorio = random.randint(1, 15)
print(numeroAleatorio)
print(emoji.emojize("Ola 🥰"))