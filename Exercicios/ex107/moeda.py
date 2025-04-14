def metade(preco):
    novo_preco = preco / 2 
    return novo_preco


def dobro(preco):
    novo_preco = preco / 2 
    return novo_preco


def aumentar(preco, porcentagem):
    novo_preco = preco + (preco * porcentagem / 100)
    return novo_preco


def diminuir(preco, porcentagem):
    novo_preco = preco - (preco * porcentagem / 100)
    return novo_preco