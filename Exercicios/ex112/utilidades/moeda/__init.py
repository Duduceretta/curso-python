def metade(preco = 0, formatar = False):
    novo_preco = preco / 2
    if formatar:
        novo_preco = moeda(novo_preco) 
    return novo_preco


def dobro(preco = 0, formatar = False):
    novo_preco = preco * 2 
    if formatar:
        novo_preco = moeda(novo_preco)
    return novo_preco


def aumentar(preco = 0, porcentagem = 0, formatar = False):
    novo_preco = preco + (preco * porcentagem / 100)
    if formatar:
        novo_preco = moeda(novo_preco)
    return novo_preco


def diminuir(preco = 0, porcentagem = 0, formatar = False):
    novo_preco = preco - (preco * porcentagem / 100)
    if formatar:
        novo_preco = moeda(novo_preco)
    return novo_preco


def moeda(preco = 0, moeda = 'R$'):
    novo_preco = f'{moeda}{preco:.2f}'.replace('.', ',')
    return novo_preco


def resumo(preco = 0, aumento = 0, reducao = 0):
    print('--' * 20)
    print('RESUMO DO VALOR'.center(40))
    print('--' * 20)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de reducao: \t{diminuir(preco, reducao, True)}')
    print('--' * 20)