#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A media de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres tem menos de 20 anos 

mediaIdade = 0
idadeHomemMaisVelho = 0
nomeHomemMaisVelho = ''
mulherMenos20Anos = 0

for i in range(0, 4):
    print('=======' + 'Novo Usuario' + '=======')
    nome = str(input('Qual o seu nome?: ')).strip()
    idade = int(input('Qual a sua idade?: '))
    sexo = str(input('Qual o seu sexo? (M ou F): ')).strip().upper()

    mediaIdade = mediaIdade + idade
    if sexo == 'F' and idade < 20:
        mulherMenos20Anos = mulherMenos20Anos + 1

    if sexo == 'M' and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        nomeHomemMaisVelho = nome

mediaIdade = mediaIdade / 4

print(f'A media de idade do grupo é de: {mediaIdade:.2f}')
print(f'O nome do homem mais velho é {nomeHomemMaisVelho} e ele tem {idadeHomemMaisVelho} anos')
print(f'{mulherMenos20Anos} mulher(es) tem menos de 20 anos')