#Escreva um programa que pergunte a quantidade de Km rodados por um carro alugado e a quantidade de dias pelos quais ele foi alugado . Calcule o preço a pagar sabendo que o carro custo 60 por dia e 0.15 por km rodado

kmPercorridos = float(input('Quantos Km foram percorridos?: '))
diasAlugado = int(input('Por quantos dias o carro foi alugado?: '))
totalValor = (kmPercorridos * 0.15) + (diasAlugado * 60)
print(f'Total de valor a pagar: RS{totalValor:.2f}')
