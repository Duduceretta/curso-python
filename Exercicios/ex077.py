#Cire um programa que tenha uma tupla com varias palavras, Depois disso voce deve mostrar para cada palavra quais sao as suas vogais

palavras = ('programador', 'bonito', 'radio', 'magia', 'cochilo', 'urubu')

for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i].upper()} temos: ', end='')
    for letra in palavras[i]:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            print(letra, end= ' ')
    