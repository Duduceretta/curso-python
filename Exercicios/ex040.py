#Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordo com a media atingida
#Abaixo de 5.0 reprovado
#Entre 5.0 e 6.9 Recuperacao
#7.0 ou superior Aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media > 7.0:
    print('Parabens voce foi aprovado')
    print(f'Sua media foi {media:.2f}')
elif media >= 5.0:
    print('Voce esta em recuperacao')
    print(f'Sua media foi {media:.2f}')
else:
    print('Infelizmente voce foi reprovado')
    print(f'Sua media foi {media:.2f}')