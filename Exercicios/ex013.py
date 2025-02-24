#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Digite o valor do seu salario: R$'))
novoSalario = salario + (salario * 0.15)
print(f'Seu salario atual é: {salario:.2f} R$')
print(f'Seu salario com bonus de 15% ficará: {novoSalario:.2f} R$')
