#Escreva um programa que pergunta o salario de um funcionario e calcule o valor de seu aumento
#Para salario superiores a 1250 calcule um aumento de 10%
#Para inferiores ou iguais aumento de 15%

salarioAtual = float(input('Digite seu salario: R$'))
if salarioAtual > 1250:
    print('Voce ganhou um bonus de 10%')
    print(f'Seu salario agora e: {salarioAtual + (salarioAtual * 0.10)}')
else:
    print('Voce ganhou um bonus de 15%')
    print(f'Seu salario agora e: {salarioAtual + (salarioAtual * 0.15)}')