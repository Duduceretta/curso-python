#Crie um programa que tenha uma funcao leiaInt, que vai funcionar de forma semelhante a funcao input do python, So que fazendo a validacao para aceitar apensa um valor numerico 

def leiaInt(str = ''):
    while True:
        entrada = input(str).strip()
        if entrada.isdigit():
            return entrada
        else:
            print('Por favor digite somente valores numericos')


#Programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
