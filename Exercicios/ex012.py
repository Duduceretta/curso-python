#Faça um algoritmo que leia o preco de um produto e mostre seu novo preco com 5% de desconto

preco = float(input('Digite o preco do produto: R$'))
novoPreco = preco - (preco * 0.05)
print(f'Preco do produto sem desconto: {preco:.2f} R$')
print(f'Preco do produto com 5% de desconto aplicado: {novoPreco:.2f} R$')
