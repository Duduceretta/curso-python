#Reescreva a funcao leiaInt do desafio 104 incluindo agora a possibilidade da digitacao de um numero de tipo invalido. Crie tambem uma funcao leiaFloat com a mesma funcionalidade

def leia_int(msg = ''):
    while True:
        try:
            numero_inteiro = int(input(msg))
        except (TypeError, ValueError):
            print('Erro, digite um numero inteiro valido')
            continue
        except (KeyboardInterrupt):
            print('O usuario preferiu nao digitar os valores')
            return 0
        else:
            return numero_inteiro


def leia_float(msg = ''):
    while True:
        try:
            numero_real = float(input(msg))
        except (ValueError, TypeError):
            print('Erro digite um numero real valido')
        except (KeyboardInterrupt):
            print('O usuario preferiu nao digitar os valores')
            return 0
        else:
            return numero_real


#Programa principal
num1 = leia_int('Digite um numero inteiro: ')
num2 = leia_float('Digite um numero real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2:.2f}')
