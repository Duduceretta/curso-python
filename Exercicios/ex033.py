#Faça um programa que leia 3 numeros e mostre qual e o maior e o menor

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'O maior numero e: {n1}, o menor e: {n3}')
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'O maior numero e: {n1}, o menor e: {n2}')
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f'O maior numero e: {n2}, o menor e: {n3}')
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f'O maior numero e: {n2}, o menor e: {n1}')
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(f'O maior numero e: {n3}, o menor e: {n1}')
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f'O maior numero e: {n3}, o menor e: {n2}')