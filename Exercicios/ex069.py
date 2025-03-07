#Crie um programa que leia o sexo e a idade de varias pessoas. A cada pessoa cadastrada o programa devera perguntar se o usuario quer ou nao continuar. No final mostre
#Quantas pessoas tem mais de 18 anos
#Quantos homens foram cadastrados
#Quantas mulheres tem menos de 20 anos

pessoasMais18 = 0
homensCadastrados = 0
mulheresMenos20 = 0

while True:
    print('=' * 30)
    print('    CADASTRAR NOVA PESSOA')
    print('=' * 30)
    idade = int(input('Qual a sua idade?: '))
    sexo = str(input('Qual o seu sexo? (F/M): ')).upper().strip()
    while sexo not in 'FM':
        print('Sexo invalido, digite novamente')
        sexo = str(input('Qual o seu sexo? (F/M): ')).upper().strip()

    if idade > 18:
        pessoasMais18 += 1
    
    if sexo == 'M':
        homensCadastrados += 1
    
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1

    resposta = str(input('Deseja cadastrar uma nova pessoa? (S/N): ')).upper().strip()
    while resposta not in 'SN':
        print('Codigo invalido, digite novamente')
        resposta = str(input('Deseja cadastrar uma nova pessoa? (S/N): ')).upper().strip()
    if resposta == 'N':
        break

print('=' * 30)
print(f'Foram cadastradas {pessoasMais18} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homensCadastrados} homens')
print(f'Foram cadstradas {mulheresMenos20} mulheres com menos de 20 anos')
print('FIM DO PROGRAMA')
print('=' * 30)
