#Faça um programa que leia nome e peso de varias pessoas guardando tudo em uma lista. No final mostre:
#Quantas pessoas foram cadastradas
#Uma listagem com as pessoas mais pesadas
#Uma listagem com as pessoas mais leves

pessoas = []
dados = []
maiorPeso = menorPeso = 0

while True:
    dados.append(str(input('Digite seu nome: ')).strip())
    dados.append(float(input('Digite seu peso (Kg): ')))

    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resposta = str(input('Deseja continuar? (S/N): ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Codigo invalido. Deseja continuar? (S/N): ')).strip().upper()

    if resposta == 'N':
        break

#Minha solucao
'''for pos, i in enumerate(pessoas):
    if pos == 0:
        maiorPeso = menorPeso = pessoas[pos][1]
    elif pessoas[pos][1] > maiorPeso:
        maiorPeso = pessoas[pos][1]
    elif pessoas[pos][1] < menorPeso:
        menorPeso = pessoas[pos][1]'''
        
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'[{p[0]}]', end=' ')

print(f'\nO menor peso foi de {menorPeso}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'[{p[0]}]', end=' ')
