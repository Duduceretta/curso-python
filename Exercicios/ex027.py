#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguindo o primeiro e ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
nomeSplitado = nome.split()
print(f'O primeiro nome e: {nomeSplitado[0]}')
print(f'O ultimo nome e: {nomeSplitado[-1]}')