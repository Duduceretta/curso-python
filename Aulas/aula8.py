#Estrutura de repeticao for
#Utilizada quando se sabe o numero de repeticoes a serem feitas

for i in range(0, 3):
    print('Oi')

for i in range(1, 7):
    print(i)

#começa o loop de tras pra frente
for i in range(6, 0, -1):
    print(i)

#vai de 0 ate 5 pulando de 2 em 2
for i in range(0, 6, 2):
    print(i)

num = int(input('Digite um numero: '))
for i in range(0, num + 1):
    print(i)

soma = 0
for i in range(0, 3):
    num = int(input('Digite um numero: '))
    soma = soma + num
print(f'A soma de todos os valores foi {soma}')
print('FIM')