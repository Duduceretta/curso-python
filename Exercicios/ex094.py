#Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista. No final mostre:
#Quantas pessoas foram cadastradas
#A media de idade do grupo
#Uma lista com todas as mulheres
#Uma lista com todas as pessoas com idade acima da media

import time

dadosPessoa = {}
pessoas = []
mediaIdade = 0

while True:
    dadosPessoa['nome'] = str(input('Nome: ')).strip()
    dadosPessoa['sexo'] = str(input('Sexo (M/F): ')).strip().upper()
    while dadosPessoa['sexo'] not in 'MF':
        dadosPessoa['sexo'] = str(input('Comando Invalido. Sexo (M/F): ')).strip().upper()
    dadosPessoa['idade'] = int(input('Idade: '))
    pessoas.append(dadosPessoa.copy())

    resposta = str(input('Deseja continuar? (S/N): ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Comando invalido. Deseja continuar? (S/N): ')).upper().strip()

    if resposta == 'N':
        print('Saindo do programa...')
        time.sleep(1)
        break

for dicionario in pessoas:
    mediaIdade += dicionario['idade']
mediaIdade = mediaIdade / len(pessoas)

print('-=-' * 15)
print(f' => Foram cadastradas {len(pessoas)} pessoas')
print(f' => A media de idade do grupo e de: {mediaIdade:.2f} anos')
print(f' => As mulheres cadastradas foram: ', end='')
for dicionario in pessoas:
    if dicionario['sexo'] == 'F':
        print(f'{dicionario['nome']}', end=' ')
print()
print(f' => Pessoas cadastradas com idade acima da Media: ')
for dicionario in pessoas:
    if dicionario['idade'] > mediaIdade:
        print(f'\tnome = {dicionario['nome']}, sexo = {dicionario['sexo']}, idade = {dicionario['idade']}')
print(f'-' * 10, '>>> FIM DO PROGRAMA <<<', '-' * 10)
