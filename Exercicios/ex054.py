#Crie um programa que leia o ano de nascimento de sete pessoas. No finalmostre quantas pessoas atingiram a maioridade e quantas nao

import datetime

anoAtual = datetime.date.today().year
Maioridade = 0
semMaioridade = 0

for i in range(0, 7):
    anoNascimento = int(input('Digite o ano do seu nascimento: '))
    idade = anoAtual - anoNascimento
    if idade >= 21:
        Maioridade = Maioridade + 1
    else:
        semMaioridade = semMaioridade + 1

print(f'{Maioridade} pessoas atingiram a maioridade')
print(f'{semMaioridade} pessoas nao atingiram a maioridade')