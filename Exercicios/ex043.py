#Desenvolva uma logica que leia o peso e a altura de uma pessoa. Calcule seu imc e mostre seu status de acordo com a tabela
#Abaixo de 18.5 abaixo do peso, entre 18.5 a 25 peso normal, 25 ate 30 sobrepeso, 30 ate 40 obesidade, acima de 40 obesidade morbida

peso = float(input('Digite o seu peso em Kg (75.8): '))
altura = float(input('Digite a sua altura em m (1.71): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu imc foi {imc:.2f} e voce esta abaixo do peso')
elif imc < 25:
    print(f'Seu imc foi {imc:.2f} e voce esta com o peso normal')
elif imc < 30:
    print(f'Seu imc foi {imc:.2f} e voce esta com sobrepeso')
    print('Cuidado')
elif imc < 40:
    print(f'Seu imc foi {imc:.2f} e voce esta com obesidade')
    print('Cuidado')
else:
    print(f'Seu imc foi {imc:.2f} e voce esta com obesidade morbida')
    print('Cuidado urgente')
    