#O mesmo professor quer sortear a ordem de apresentacao de trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
import random

nome1 = input('Digite o nome do aluno 1: ')
nome2 = input('Digite o nome do aluno 2: ')
nome3 = input('Digite o nome do aluno 3: ')
nome4 = input('Digite o nome do aluno 4: ')
alunos = [nome1, nome2, nome3, nome4]
print(f'A ordem de apresentacao sera: {random.sample(alunos, 4)}')
