#Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere dolar = 5.74

valor = float(input('Quantos reais voce tem? R$: '))
dolares = valor / 5.74
print(f'Com {valor:.2f} reais, voce consegue comprar {dolares:.2f} dolares')
