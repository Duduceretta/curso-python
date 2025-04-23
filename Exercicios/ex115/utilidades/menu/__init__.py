from time import sleep
from utilidades.validacao import leia_int


def menu_principal():
    print('--' * 20)
    print('MENU PRINCIPAL'.center(40))
    print('--' * 20)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do Sistema')
    print('--' * 20)
    opcao = leia_int('Sua opcao: ')
    return opcao


def mensagem_despedida():
    print('--' * 20)
    print('Saindo do Sistema... Até logo!'.center(40))
    print('--' * 20)
    sleep(1)
    