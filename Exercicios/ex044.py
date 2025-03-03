#Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preco normal e condicao de pagamento
#a vista dinheiro/cheque - 10% de desconto, a vista no cartao 5% de desconto, em ate 2x no cartao preco normal, 3x ou mais no cartao 20% de juros

preco = float(input('Qual o preco do produto?: R$'))
print('-' * 40)
print('Selecione a forma de pagamento')
print('Digite 1 para pagar a vista (dinehiro / cheque)')
print('Digite 2 para pagar a vista (cartao)')
print('Digite 3 para pagar em ate 2x no cartao')
print('Digite 4 para pagar em 3x ou mais no cartao')
print('-' * 40)
escolha = int(input('Digite a forma de pagamento: '))
print('-' * 40)

if escolha == 1:
    novoPreco = preco - (preco * 0.10)
    print('Opcao escolhida: pagamento a vista (dinheiro / cheque)')
    print(f'Preco do produto R${preco:.2f}')
    print(f'Habilitado 10% de desconto')
    print(f'Preco final a ser pago R${novoPreco:.2f}')
elif escolha == 2:
    novoPreco = preco - (preco * 0.05)
    print('Opcao escolhida: pagamento a vista (cartao)')
    print(f'Preco do produto R${preco:.2f}')
    print(f'Habilitado 5% de desconto')
    print(f'Preco final a ser pago R${novoPreco:.2f}')
elif escolha == 3:
    parcela = preco / 2
    print('Opcao escolhida: pagamento no cartao em ate 2x')
    print(f'Preco do produto R${preco:.2f}, parcelado em 2x de R${parcela:.2f} no cartao')
    print(f'Sem desconto')
    print(f'Preco final a ser pago R${preco:.2f}')
elif escolha == 4:
    parcela = int(input('Em quantas parcelas voce quer pagar? (3 ate 12): '))
    juros = preco * 0.20
    novoPreco = preco + juros
    custoParcela = novoPreco / parcela
    print('Opcao escolhida: pagamento no cartao 3x ou mais')
    print(f'Preco do produto R${preco:.2f}')
    print(f'Juros de 20% ao mes, total de parcelas: {parcela}')
    print(f'Cada parcela custara: R${custoParcela:.2f}')
    print(f'Preco final a ser pago R${novoPreco:.2f}')
else:
    print('Escolha uma opcao valida')
print('-' * 40)
