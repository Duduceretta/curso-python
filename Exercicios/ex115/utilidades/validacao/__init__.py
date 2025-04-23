def leia_int(msg = ''):
    valido = False
    while not valido:
        try:
            numero_inteiro = input(msg).strip()
            numero_inteiro = int(numero_inteiro)
            if numero_inteiro < 0:
                raise ValueError("Digite um número inteiro positivo.")
            return numero_inteiro
        except (TypeError, ValueError):
            print('Erro, digite um numero inteiro valido')
        except (KeyboardInterrupt):
            print('\nEntrada cancelada pelo usuário.')
            numero_inteiro = 0
            break
        else:
            valido = True
    return numero_inteiro


def leia_str(msg = ''):
    valido = False
    while not valido:
        try:
            string = input(msg).strip()
            if not string.replace(' ', '').isalpha():
                raise ValueError("Digite apenas letras, sem números ou símbolos.")
            return string
        except ValueError as e:
            print(f'Erro: {e}')
        except KeyboardInterrupt:
            print('\nEntrada cancelada pelo usuário.')
            return ''
            