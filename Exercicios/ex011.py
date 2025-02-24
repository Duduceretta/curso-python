#Faça um programa que leia a largura e a altura de uma parede em metros e calcule sua area e quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta 2m²

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = altura * largura
qtdDeTinta = area / 2
print(f'A area da parede é: {area:.2f} m²')
print(f'A quantidade de litros de tinta para a pintura é: {qtdDeTinta:.2f} l')
