#Tipos primitivos e Saida de Dados
#
#int = numeros inteiros
#float = numeros reais
#str = strings, palavras
#bool = booleanos, False, True

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
soma = n1 + n2
print(f'A soma entre {n1} e {n2} = {soma}')

print('======================================')

#Verifica se o n3 é um numero
n3 = input('Digite um numero: ')
print(n3.isnumeric())

#Verifica se o n4 é um caracter do alfabeto
n4 = input('Digite um numero: ')
print(n4.isalpha())

#Verifica se o n5 é um caracter do alfabeto numerico
n5 = input('Digite um numero: ')
print(n5.isalnum())

#Verifica se o n6 é somente letras maiusculas
n6 = input('Digite um numero: ')
print(n6.isupper())