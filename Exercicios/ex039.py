#Faça um programa que leia o ano de nascimento de um jovem e informa de acordo com sua idade
#Se ele ainda vai se alistar no serviço militar
#Se e a hora de se alistar
#Se ja passou do tempo de alistamento
#Tambem devera mostrar o tempo q falta ou que passou do prazo

import datetime

anoAtual = datetime.date.today().year
anoNascimento = int(input('Digite seu ano de nascimento: '))
if anoAtual - anoNascimento < 18:
    print(f'Voce nasceu em {anoNascimento} e tem {anoAtual - anoNascimento} anos em {anoAtual}')
    print('O momento de se alistar esta chegando')
    print(f'Faltam {18 - (anoAtual - anoNascimento)} anos para se alistar')
elif anoAtual - anoNascimento == 18:
    print(f'Voce nasceu em {anoNascimento} e tem {anoAtual - anoNascimento} anos em {anoAtual}')
    print('Chegou o momento de se alistar')
    print('Faca ja a sua inscricao')
else:
    print(f'Voce nasceu em {anoNascimento} e tem {anoAtual - anoNascimento} anos em {anoAtual}')
    print('Voce ja deveria ter se alistado')
    print(f'Voce esta atrasado {(anoAtual - anoNascimento) - 18} ano(s) para o alistamento')

