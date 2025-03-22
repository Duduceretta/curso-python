#Faça um programa que tenha uma funcao chamada area, que receba as dimensoes de um terreno retangular (largura e comprimento) e mostre a area do terreno

def area(larg, comp):
    area = larg * comp
    print(f'A area de um terreno {larg:.1f}x{comp:.1f} e de {area:.1f}m²')


#Programa Principal
print('Controle de Terrenos')
print('--' * 10)
largura = float(input('LARGURA em (m): '))
comprimento = float(input('COMPRIMENTO em (m): '))
area(largura, comprimento)
