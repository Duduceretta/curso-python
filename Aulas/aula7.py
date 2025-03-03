#Condicoes aninhadas

nome = str(input('Qual o seu nome?: '))
if nome == 'Eduardo':
    print('Nome bonitu')
elif nome == 'Joao' or nome == 'Ana':
    print('Nome bem comum no Brasil')
elif nome in 'Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal')
print(f'Tenha um bom dia {nome}')