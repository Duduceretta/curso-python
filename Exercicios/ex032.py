#Faça um programa que leia um ano qualquer e mostra se ele é bissexto

import datetime

ano = int(input('Digite um ano, Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O Ano {ano} bissesxto')
        else:
            print(f'O Ano {ano} nao bissexto')
    else:
        print(f'O Ano {ano} bissexto')
else:
    print(f'O Ano {ano} nao bissexto')