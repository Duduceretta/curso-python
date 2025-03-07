#Faça um programa que jogue par ou impar com o computador, o jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

import random
import time

contaVitorias = 0

while True:
    print('-' * 20)
    print(' JOGO PAR OU IMPAR')
    print('-' * 20)
    numeroComputador = random.randint(0, 10)
    numeroJogador = int(input('Digite um numero: '))
    parImpar = str(input('Voce escolhe par ou impar? (P/I): ')).strip().upper()
    while parImpar not in 'PI':
        parImpar = str(input('Invalido. Voce escolhe par ou impar? (P/I): ')).strip().upper()
    print('Verificando resultado....')
    time.sleep(2)

    print('=' * 20)
    soma = numeroJogador + numeroComputador
    if soma % 2 == 0 and parImpar == 'P':
        print(f'Eu escolhi {numeroComputador} e voce {numeroJogador}')
        print(f'A soma deu {soma}, e voce escolheu Par')
        print('Voce ganhou!!!')
        print('=' * 20)
        contaVitorias += 1
    elif soma % 2 != 0 and parImpar == 'I':
        print(f'Eu escolhi {numeroComputador} e voce {numeroJogador}')
        print(f'A soma deu {soma}, e voce escolheu Impar')
        print('Voce ganhou!!!')
        print('=' * 20)
        contaVitorias += 1
    elif soma % 2 != 0 and parImpar == 'P':
        print(f'Eu escolhi {numeroComputador} e voce {numeroJogador}')
        print(f'A soma deu {soma}, e voce escolheu Par')
        print('Eu ganhei')
        break
    else:
        print(f'Eu escolhi {numeroComputador} e voce {numeroJogador}')
        print(f'A soma deu {soma}, e voce escolheu Impar')
        print('Eu ganhei')
        break
    soma = 0

print('=' * 20)
print('FIM DO JOGO')
print(f'Voce obteve {contaVitorias} vitorias consecutivas')
print('=' * 20)
