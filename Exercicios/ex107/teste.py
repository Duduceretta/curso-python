#Crie um modulo chamado moeda.py que tenhas as funcoes incorporadas aumentar, diminuir, dobro e metade
#Faça tambem um programa que importe esse modulo e use algumas dessas funcoes

import moeda

preco = float(input('Digite o preco: R$'))
print(f'A metade de {preco} e {moeda.metade(preco)}')
print(f'O dobro de {preco} e {moeda.dobro(preco)}')
print(f'Aumentado 10% temos {moeda.aumentar(preco, 10)}')
print(f'Reduzindo 13% temos {moeda.diminuir(preco, 13)}')
