#Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random

nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')
nome4 = input('Digite o nome do aluno 4: ')
alunos = [nome1, nome2, nome3, nome4]
print(f'O escolhido para apagar o quadro foi: {random.choice(alunos)}')