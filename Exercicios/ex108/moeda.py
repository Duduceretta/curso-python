def metade(preco = 0):
    novo_preco = preco / 2 
    return novo_preco


def dobro(preco = 0):
    novo_preco = preco * 2 
    return novo_preco


def aumentar(preco = 0, porcentagem = 0):
    novo_preco = preco + (preco * porcentagem / 100)
    return novo_preco


def diminuir(preco = 0, porcentagem = 0):
    novo_preco = preco - (preco * porcentagem / 100)
    return novo_preco


def moeda(preco = 0, moeda = 'R$'):
    novo_preco = f'{moeda}{preco:.2f}'.replace('.', ',')
    return novo_preco