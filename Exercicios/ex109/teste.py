#Modifique as funcoes que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor retornado por elas vai ser ou nao formatado pela funcao moeda desenvolvida no 108

import moeda

preco = float(input('Digite o preco: R$'))
print(f'A metade de {moeda.moeda(preco)} e {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} e {moeda.dobro(preco, True)}')
print(f'Aumentado 10% temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13% temos {moeda.diminuir(preco, 13, True)}')
