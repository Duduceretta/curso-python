#Crie um programa que tenha uma funcao fatorial que receba dois parametros: o primeiro que indique o numero que quer calcular e a outra chamada show que sera um valor logico opcional indicando se sera ou nao mostrado na tela o processo de calculo do fatorial

def fatorial(num = 1, show = False):
    """Calcula o fatorial de um numero n
    Args:
        num (int): numero para calcular o fatorial
        show (bool, optional): Mostra o processo do fatorial. Defaults to False.
    Returns:
        int: Retorna o fatorial de n
    """
    # fat = 1
    # if show:
    #     for i in range(num, 0, -1):
    #         #fat = fat * i
    #         print(f'{i}', end='')
    #         print(' x ' if i > 1 else ' = ', end= '')
    #     fat *= i
    #     #return fat
    # else:
    #     for i in range(num, 1, -1):
    #         fat = fat * i
    #     return fat 

    fat = 1
    for i in range(num, 0, -1):
        if show:
            print(f'{i}', end=' x ' if i > 1 else ' = ')
        fat *= i
    return fat


#Programa principal
print(fatorial(5, True))
