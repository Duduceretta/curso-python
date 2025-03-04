#Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares, Se o valor digitado for impar desconsidere-o

soma = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i} numero: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma total dos numeros pares digitados e: {soma}')   