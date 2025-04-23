#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples
#O sistema so vai ter duas opcoes: cadastrar uma nova pessoa e listar todas as pessoas cadastradas

from time import sleep
from utilidades.menu import menu_principal, mensagem_despedida
from utilidades.arquivo import criar_arquivo, cadastrar_pessoa_arquivo, ver_pessoas_cadastradas

nome_arquivo = 'sistema_cadastro.txt'
criar_arquivo(nome_arquivo)

while True:
    opcao = menu_principal()

    if opcao == 1:
        ver_pessoas_cadastradas(nome_arquivo)
    elif opcao == 2:
        cadastrar_pessoa_arquivo(nome_arquivo)
    elif opcao == 3:
        mensagem_despedida()
        break    
    else:
        print(f'Opcao {opcao} invalida')
        sleep(1)
