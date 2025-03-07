#Interrompendo laço de repetição while

numero = 0
soma = 0
while True:
    numero = int(input('Digite um numero: '))
    if numero == 999:
        break #Quebra o laço se o numero digitado for 999
    soma = soma + numero
print(f'A soma dos valores foi: {soma}')
