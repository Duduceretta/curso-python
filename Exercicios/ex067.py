#Faça um programa que mostre a tabuada de varios numeros um de cada vez, para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo

print('======Tabuada======')
while True:
    numero = int(input('Digite um numero para ver sua tabuada: '))
    if numero < 0:
        break
    
    print('--' * 20)
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('--' * 20)

print('Fim do programa')
