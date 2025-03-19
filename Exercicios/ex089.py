#Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente

import time

listaPrincipal = []
media = 0

while True:
    nome = str(input('Digite o nome do aluno(a): ')).strip()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    listaPrincipal.append([nome, [nota1, nota2], media])

    resposta = str(input('Deseja continuar? (S/N): ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Codigo invalido. Deseja continuar? (S/N): ')).upper().strip()

    if resposta == 'N':
        print('-=-' * 10)
        print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
        print('---' * 10)

        for pos, aluno in enumerate(listaPrincipal):
            print(f'{pos:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')          
        
        while True:
            print('---' * 10)
            r = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

            if r == 999:
                break
            if r >= len(listaPrincipal) or r < 0:
                print('Aluno nao existente!')
            else:
                print(f'As notas de {listaPrincipal[r][0]} foram {listaPrincipal[r][1]}')
        print('Saindo do programa...')
        time.sleep(1)
        break
print('--' * 5, ' < Fim do programa > ', '--' * 5)
