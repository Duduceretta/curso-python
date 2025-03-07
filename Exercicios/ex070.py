#Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se o usuario vai continuar. No final mostre
#Qual e o total gasto
#Quantos produtos custam mais de 1000
#Qual o nome do produto mais barato

totalGasto = 0
custaMais1000 = 0
nomeMaisBarato = ''
precoMaisBarato = 0
contador = 0

while True:
    print('=' * 20)
    print('      LOJINHA')
    print('=' * 20)
    nome = str(input('Nome do produto: ')).strip().lower()
    preco = float(input('Preco do produto: R$'))

    if contador == 0 or preco < precoMaisBarato:
        nomeMaisBarato = nome
        precoMaisBarato = preco
  
    totalGasto += preco

    if preco > 1000:
        custaMais1000 += 1

    contador += 1
    resposta = str(input('Quer adicionar mais produtos? (S/N) ')).strip().upper()
    while resposta not in 'SN':
        print('Codigo invalido, digite novamente')
        resposta = str(input('Quer adicionar mais produtos? (S/N) ')).strip().upper()

    if resposta == 'N':
        break

print('=' * 30)
print(f'Total gasto com as compras R${totalGasto:.2f}')
print(f'Há {custaMais1000} produtos que custam mais de R$1000')
print(f'O produto mais barato foi {nomeMaisBarato} e custou R${precoMaisBarato:.2f}')
print('FIM DO PROGRAMA')
print('=' * 30)
