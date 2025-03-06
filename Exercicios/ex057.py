#Faça um programa que leia o sexo de uma pessoa, mas so aceita os valores 'M' ou 'F', caso esteja errado peça a digitação novamente ate ter um valor correto

print('=======Inicio do Programa=======')
sexo = input('Digite o seu sexo: (M/F): ').upper().strip()
while sexo != 'F' and sexo != 'M': #not in 'MmFf'
    print('Sexo invalido, digite novamente')
    sexo = input('Informe seu sexo novamente: (F/M) ').upper().strip()
print('Sexo valido')
print(f'O sexo digitado foi {sexo}')
