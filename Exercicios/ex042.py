#Refaca o exercicio 35 dos triangulos. acrescentando o recurso de mostrar qual tipo de triangulo sera formado
#Equilatero, isoceles, Escaleno

lado1 = int(input('Digite o tamanho do lada1: '))
lado2 = int(input('Digite o tamanho do lada2: '))
lado3 = int(input('Digite o tamanho do lada3: '))
if(lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
    print('É possivel formar um triangulo')
    if lado1 == lado2 == lado3:
        print('O triangulo é do tipo equilatero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('O triangulo é do tipo isoceles')
    else:
        print('O triangulo é do tipo escaleno ')
else:
    print('Nao é possivel formar um triangulo')