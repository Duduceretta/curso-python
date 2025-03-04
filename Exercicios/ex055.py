#Faca um programa que leia o peso de cinco pessoas no final mostre qual foi o maior e o menor peso lidos

maiorPeso = -9999999
menorPeso = 9999999

for i in range(1, 6):
    peso = float(input(f'Digite o {i}º peso: '))
    if peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso

print(f'O maior peso digitado foi: {maiorPeso:.2f}Kg')
print(f'O menor peso digitado foi: {menorPeso:.2f}Kg')