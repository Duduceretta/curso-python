#Adapte o codigo do desafio 107, criando uma funcao adicional chamada moeda que consiga mostrar os valores como um valor monetario formatado

import moeda

preco = float(input('Digite o preco: R$'))
print(f'A metade de {moeda.moeda(preco)} e {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} e {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentado 10% temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'Reduzindo 13% temos {moeda.moeda(moeda.diminuir(preco, 13))}')
