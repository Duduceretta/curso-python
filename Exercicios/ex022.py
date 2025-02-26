#Crie um programa que leia o nome completo de uma pessoa e mostre
#O nome com todas letras maiusculas
#O nome com todas minusculas
#Quantas letras ao todo, sem considerar espaços
#Quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ').strip()
nomeSplitado = nome.split()
print(f'Nome com todas as letras maiusculas: {nome.upper()}')
print(f'Nome com todas as letras minusculas: {nome.lower()}')
print(f'Quantidade de letras ao todo: {len(nome.replace(' ',''))}')
print(f'Quantidade de letras do primeiro nome: {len(nomeSplitado[0])}')
