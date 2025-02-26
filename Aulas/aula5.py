#Condições
nome = str(input('Qual e o seu nome? '))
if nome == 'Eduardo':
    print('Que lindo nome')
else:
    print('Seu nome e tao normal')
print(f'Seja bem vindo {nome}')

n1 = float(input('Digite a nota1: '))
n2 = float(input('Digite a nota2: '))
media = (n1 + n2) / 2
print(f'A sua media foi {media:.1f}')
if media >= 6:
    print('Media boa')
else:
    print('Estude mais')
