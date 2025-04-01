#Crie um programa que tenha uma funcao chamada voto que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatorio nas eleicoes

#Utiliza a importacao na execucao inteira do programa
#import datetime


def voto(anoNasc):
    """Retorna uma String dizendo que tipo de voto a pessoa pode fazer com base na idade
    Args:
        anoNasc (int): ano de nascimento da pessoa
    Returns:
        String: retorna uma frase com base na idade calculada
    """
    #Escopo de importacao, economiza memoria, utiliza a biblioteca so quando a funcao e chamada
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if idade < 16:
        return f'Com {idade} anos o voto e NEGADO'   
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} ano o voto e OPCIONAL'
    else:
        return f'Com {idade} anos o voto e OBRIGATORIO'


#Programa principal
anoNascimento = int(input('Em que ano voce nasceu?: '))
print(voto(anoNascimento))
