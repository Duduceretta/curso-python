def ler_dinheiro(msg):
    valido = False
    while not valido:
        preco = str(input(msg)).replace(',', '.').strip()
        if preco.isalpha() or preco == '':
            print(f'ERRO "{preco}" e um preco invalido!')
        else:
            valido = True
            return float(preco)

