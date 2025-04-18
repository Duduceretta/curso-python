#Reescreva a funcao leiaInt do desafio 104 incluindo agora a possibilidade da digitacao de um numero de tipo invalido. Crie tambem uma funcao leiaFloat com a mesma funcionalidade

def leia_int(msg = ''):
    valido = False
    while not valido:
        try:
            numero_inteiro = input(msg).replace(',', '.').strip()
            numero_inteiro = int(numero_inteiro)
        except (TypeError, ValueError):
            print('Erro, digite um numero inteiro valido')
        except (KeyboardInterrupt):
            print('O usuario preferiu nao digitar os valores')
            numero_inteiro = 0
            break
        else:
            valido = True
    return numero_inteiro


def leia_float(msg = ''):
    valido = False
    while not valido:
        try:
            numero_real = input(msg).replace(',' , '.').strip()
            numero_real = float(numero_real)
        except (ValueError, TypeError):
            print('Erro digite um numero real valido')
        except (KeyboardInterrupt):
            print('O usuario preferiu nao digitar os valores')
            numero_real = 0
            break
        else:
            valido = True
    return numero_real


#Programa principal
num1 = leia_int('Digite um numero inteiro: ')
num2 = leia_float('Digite um numero real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2:.2f}')
