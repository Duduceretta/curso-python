#Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = input('Digite seu nome completo: ').strip().lower()
nomeSplitado = nome.split()
print(f'Voce tem Silva no nome? {'silva' in nomeSplitado}')