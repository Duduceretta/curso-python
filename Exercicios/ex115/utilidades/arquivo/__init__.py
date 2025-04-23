from time import sleep
from utilidades.validacao import leia_int, leia_str


def criar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'x') as arquivo:
            pass
    except FileExistsError:
        pass


def cadastrar_pessoa_arquivo(nome_arquivo):
    print('--' * 20)
    print('NOVO CADASTRO'.center(40))
    print('--' * 20)
    nome = leia_str('Nome: ')
    idade = leia_int('Idade: ')
    try:
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(f'{nome.ljust(30)}{idade} anos\n')
            print(f'Novo registro de {nome} adicionado')
    except Exception as e:
        print(f'Erro ao escrever no arquivo: {e}')
    sleep(1)


def ver_pessoas_cadastradas(nome_arquivo):
    print('--' * 20)
    print('PESSOAS CADASTRADAS'.center(40))
    print('--' * 20)
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print('Nao ha pessoas cadastradas!')
            else:
                for linha in linhas:
                    print(linha, end='')
    except FileNotFoundError:
        print('Arquivo nao encontrado')
    sleep(1)
