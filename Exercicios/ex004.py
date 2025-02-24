#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas informacoes possiveis sobre ele

tipo = input('Digite alguma coisa: ')
print(f'O tipo primitivo do que voce digitou é: {type(tipo)}')
print(f'É alfa-numerico?: {tipo.isalnum()}')
print(f'É numerico?: {tipo.isnumeric()}')
print(f'É decimal?: {tipo.isdecimal()}')
print(f'É tudo minisculo?: {tipo.islower()}')
print(f'É tudo maiusculo?: {tipo.isupper()}')
print(f'É espaço?: {tipo.isspace()}')
print(f'É um digito?: {tipo.isdigit()}')
print(f'É alfabetico?: {tipo.isalpha()}')
print(f'É captalizada(minusculas e maiusculas)?: {tipo.istitle()}')
