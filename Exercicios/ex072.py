#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensao, de zero ate 20
#Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lá por extenso

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Voce digitou o numero {tupla[numero]}')
        resposta = str(input('Deseja continuar? (S/N): ')).strip().upper()
        while resposta not in 'SN':
            resposta = str(input('Comando invalido. Deseja continuar? (S/N): ')).strip().upper()
        if resposta == 'N':
            break
    else:
        print('Numero nao esta no intervalo.', end=' ') 
            