#Desenvolva um programa que pergunta a distancia de uma viagem em km
#Calcule o preco da passagem cobrando 0.50 por km para viagens de ate 200km
#e 0.45 para viagens mais longas

distanciaViagem = float(input('Digite a distancia da viagem em Km: '))
if distanciaViagem > 200:
    precoPassagem = 0.45 * distanciaViagem
    print('Viagem de mais de 200km')
    print(f'Valor da passagem: R${precoPassagem:.2f}')
else:
    precoPassagem = 0.50 * distanciaViagem
    print('Viagem de até 200km')
    print(f'Valor da passagem: R${precoPassagem:.2f}')