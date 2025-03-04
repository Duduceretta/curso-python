#Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 ate 500

soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma = soma + i
print(f'A soma entre todos os numeros impares e multiplos de 3 foi {soma}')