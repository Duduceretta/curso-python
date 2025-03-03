#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestacao mensal sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado

valorCasa = float(input('Valor da casa a ser comprada: R$'))
salarioComprador = float(input('Valor do seu salario mensal: R$'))
anos = int(input('Em quantos anos voce quer pagar?: '))
prestacaoMensal = valorCasa / (anos * 12)
if prestacaoMensal > salarioComprador * 0.30:
    print('Prestacao mensal maior que o seu salario')
    print('Parcela invalida, Emprestimo recusado')
    print(f'Prestacao mensal: {prestacaoMensal:.2f}, Salario do comprador: {salarioComprador}')
else:
    print('Parcela valida, Emprestimo autorizado')
    print(f'Prestacao mensal: {prestacaoMensal:.2f}, Salario do comprador: {salarioComprador}')