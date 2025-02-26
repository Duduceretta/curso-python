#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo q ele foi multado
#A multa vai custar 7.00 para cada km acima do limite

velocidade = float(input('Digite a velocidade do carro em Km/h: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Acima do limite de Velocidade')
    print('VOCE FOI MULTADO')
    print(f'A multa devera ser paga no valor de: R${multa:.2f}')
else:
    print('Abaixo do limite de velocidade, siga sua viagem')