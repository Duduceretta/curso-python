#Faça um programa que tenha uma funcao chamada escreva que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'{msg.center(tam)}')
    print('-' * tam)


#Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de python no youtube')
escreva('CeV')
