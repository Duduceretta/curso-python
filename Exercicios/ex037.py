#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao:
#1 - binario
#2 - octal
#3 - hexadecimal

print('-=-' * 20)
print('Ola seja bem vindo ao programa de conversao de bases!!')
numero = int(input('Digite o numero para ser convertido: '))
print('Agora escolha uma das bases de conversao abaixo')
print('Digite 1 para converter para binario')
print('Digite 2 para converter para octal')
print('Digite 3 para converter para hexadecimal')
escolha = int(input('Digite aqui a opcao escolhida: '))
if escolha == 1:
    print(f'O numero {numero} convertido para binario fica: {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O numero {numero} convertido para octal fica: {oct(numero)[2:]}')
elif escolha == 3:
    print(f'O numero {numero} convertido para hexadecimal fica: {hex(numero)[2:]}')
else:
    print('Desculpe, opcao nao encontrada!')
    print('Por favor tente outra!')
print('-=-' * 20)