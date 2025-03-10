#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos precos, na sequencia
#No final mostre uma listagem de preços organizando os dados em forma tabular

produtos = ('Pão', 1.75, 'Lápis', 7.99, 'Compasso', 9.99, 'Mouse', 50.00)

print('--' * 20)
print(f'{'Listagem de Produtos':^40}')
print('--' * 20)
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<20}.............R$ {produtos[i + 1]:>1.2f}')
print('--' * 20)
