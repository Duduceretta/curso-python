#Refaca o ex009 mostrando a tabuada de um numero que o usuario escolher so que agora utilizando um laço for

numero = int(input('Digite um numero para ver a tabuada: '))
frase = 'TABUADA'
print(frase.center(20, '='))
for i in range(1, 11):
    print(f'{numero} * {i} = {numero * i}')
print('=' * 20)