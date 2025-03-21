#Crie um programa que leia nome, ano de nascimento, e carteira de trabalho e cadastre-os (com idade) em um dicionario, se por acaso o CTPS for diferente de 0, o dicionario tambem recebera o ano de contratacao e o salario
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de contribuicao)

import datetime

anoAtual = datetime.datetime.today().year
ficha = {}

ficha['nome'] = str(input('Nome: ')).strip()
anoNascimento = int(input('Ano de Nascimento: '))
ficha['idade'] = anoAtual - anoNascimento
ficha['ctps'] = int(input('Carteira de Trabalho (0 se nao tiver): '))
if ficha['ctps'] == 0:
    print('-=' * 30)
    for key, value in ficha.items():
        print(f' -- {key} tem o valor {value}')
else:
    ficha['contratacao'] = int(input('Ano de contratacao: '))
    while ficha['contratacao'] <= anoNascimento:
        ficha['contratacao'] = int(input('Informacao invalida. Ano de contratacao: '))
    ficha['salario'] = float(input('Salario: R$'))
    ficha['aposentadoria'] = (ficha['contratacao'] + 35) - anoNascimento

    print('-=' * 30)
    for key, value in ficha.items():
        print(f' -- {key} tem valor {value}')
