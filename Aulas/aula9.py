#Estrutura de repeticao while
#Utilizada quando nao se sabe o numero exato de repeticoes

i = 1
while i < 10:
    print(i)
    i += 1
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('Acabou')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? (S/N): ')).upper()
print('Voce saiu do loop')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Voce digitou {par} numeros pares e {impar} numeros impares') 