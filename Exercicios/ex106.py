#Faça um mini sistema que utilize o interactive help do python. O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar Fim o programa se encerrara
def mensagemSistemaAjuda(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


def exibeComando(c):
    mensagemSistemaAjuda(f'Acessando manual da funcao {c}')
    print(help(c))


#Programa principal
while True:
    mensagemSistemaAjuda('Sistema de Ajuda PyHelp')
    comando = str(input('Funcao ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        break
    else:
        exibeComando(comando)    
mensagemSistemaAjuda('Ate Logo')
