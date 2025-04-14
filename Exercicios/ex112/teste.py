#Dentro do pacote utilidades temos um modulo chamado dado. Crie uma funcao chamada leiadinheiro que seja capaz de funcionar como a funcao input mas com uma validacao de dados apenas valores que sejam monetarios
import sys
sys.path.append('.')  # Adiciona o diretório atual ao path

from utilidades.moeda.__init import *
from utilidades.dado import ler_dinheiro

preco = ler_dinheiro('Digite o preco: R$')
resumo(preco, 20, 12)

