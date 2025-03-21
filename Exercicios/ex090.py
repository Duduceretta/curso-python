#Faça um programa que leia nome e media de um aluno. Guardando tambem a situacao em um dicionario. No final mostre o conteudo na tela

ficha = {}
ficha['nome'] = str(input('Nome: ')).strip()
ficha['media'] = float(input(f'Media de {ficha["nome"]}: '))
if ficha['media'] >= 7:
    ficha['situacao'] = 'Aprovado'
elif ficha['media'] >= 5:
    ficha['situacao'] = 'Recuperacao'
else:
    ficha['situacao'] = 'Reprovado'
print('-=' * 30)
for key, value in ficha.items():
    print(f' -- {key} e igual a {value}')

'''print(f'O nome e igual a {ficha["nome"]}')
print(f'Media igual a {ficha["media"]}')
print(f'Situacao e igual a {ficha["situacao"]}')'''
