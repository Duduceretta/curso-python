#Modulos e pacotes
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(F'O fatorial de {num} e {fat}')
print(F'O dobro de {num} e {numeros.dobro(num)}')
