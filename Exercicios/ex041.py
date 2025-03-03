#A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
#Ate 9 anos mirim, Ate 14 anos infantil, Ate 19 junior, Ate 20 senior e acima Master

import datetime

anoAtual =  datetime.datetime.today().year
anoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = anoAtual - anoNascimento

if idade <= 9:
    print(f'Sua idade e: {idade}')
    print('Voce entrou para a categoria mirim')
elif idade <= 14:
    print(f'Sua idade e: {idade}')
    print('Voce entrou para a categoria infantil')
elif idade <= 19:
    print(f'Sua idade e: {idade}')
    print('Voce entrou para a categoria junior')
elif idade <= 25:
    print(f'Sua idade e: {idade}')
    print('Voce entrou na categoria senior')
else:
    print(f'Sua idade e: {idade}')
    print('Parabens, voce e um master')
    