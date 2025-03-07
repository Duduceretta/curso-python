#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual o valor a ser sacado (int) e o programa vai informar quantas cedulas de cada valor serao entregues
#Considere que o caixa possui cedulas de 50, 20, 10 e 1

valor = float(input('Digite o valor para ser sacado: '))
conta50 = 0
conta20 = 0
conta10 = 0
conta1 = 0
valorRestante = valor

while True:
    conta50 = valor // 50
    valorRestante = valorRestante % 50
    
    if conta50 != 0:
        print(f'Foram sacadas {conta50} notas de R$50')

    conta20 = valorRestante // 20
    valorRestante = valorRestante % 20
    
    if conta20 != 0:
        print(f'Foram sacadas {conta20} notas de R$20')

    conta10 = valorRestante // 10
    valorRestante = valorRestante % 10

    if conta10 != 0:
        print(f'Foram sacadas {conta10} notas de R$10')

    conta1 = valorRestante // 1
    valorRestante = valorRestante % 1

    if conta1 != 0:
        print(f'Foram sacadas {conta1} notas de R$1')

    if valorRestante == 0:
        break    
