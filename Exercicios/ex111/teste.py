#Crie um pacote chamado utilidades que tenha dois modulos internos chamados moeda e dado.
#Transfira todas as funcoes utilizadas nos desafios 107, 108, e 109 para o primeiro pacote

from utilidades.moeda import resumo

preco = float(input('Digite o preco: R$'))
resumo(preco, 20, 12)

