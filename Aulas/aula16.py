#Funcoes (parte 2)

#Comando para ver as documentacoes das funcoes de python
#help()
#Outra maneira utilizando .__doc__
#print(input.__doc__)

#Docstrings, usada para fazer documentacao de funcoes no codigo em python
def contador(i, f, p):
    """ -> Faz uma contagem e mostra na tela
    Args:
        i (int): inicio da contagem
        f (int): fim da contagem
        p (int): passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')

contador(1, 10 , 2)
#help(contador)

#Parametros opcionais, seta valores default caso o usuario nao informar o parametro
def soma(a = 0, b = 0, c = 0):
    """ -> Faz a soma de tres numeros e mostra na tela
    Args:
        a (float, optional): Primeiro valor. Defaults to 0.
        b (float, optional): Segundo valor. Defaults to 0.
        c (float, optional): Terceiro valor. Defaults to 0.
    """
    soma = a + b + c
    print(f'A soma vale: {soma}')

soma(3.5, 2, 3.1)
soma()

#Escopo de variaveis (variaveis globais e locais)
def teste(b):
    # x é uma variavel local, foi definida dentro da funcao teste
    #global serve para modificar o valor de x no programa principal 
    #global x
    x = 9
    print(f'Na funcao teste x vale {x}')
    print(f'Na funcao teste n vale {n}')


# n é uma variavel global
# x nao é afetada pela funcao teste
n = 2
x = 5
print(f'No programa principal n vale {n}')
teste(x)
print(f'No programa principal x vale {x}')

#Retorno de funcoes
def somar2(a=0, b=0, c=0):
    """ -> Soma 3 numeros
    Args:
        a (float, optional): Primeiro valor. Defaults to 0.
        b (float, optional): Segundo valor. Defaults to 0.
        c (float, optional): Terceiro valor. Defaults to 0.

    Returns:
        int: retorna a soma de a + b + c
    """
    soma2 = a + b + c
    return soma2

r1 = somar2(1, 2, 3)
r2 = somar2(4, 5)
r3 = somar2(1, 1)

print(f'Os valores dos meus calculos foram {r1}, {r2}, {r3}')


def fatorial(num = 1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} e {fatorial(n)}')


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero '))
print(par(num))

if par(num):
    print('É par')
else:
    print('Nao é par')
