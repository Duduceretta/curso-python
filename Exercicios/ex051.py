#Desenvolva um programa que leia o primeiro termo e a razao de uma PA, no final mostre os 10 primeiros termos dessa progressao

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
print('Progressao Aritmetica: ')
print(f'{primeiroTermo}', end=' -> ')

for i in range(0, 9):
    print(f'{primeiroTermo + razao}', end=' -> ')
    primeiroTermo = primeiroTermo + razao
print('ACABOU')
