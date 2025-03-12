#Crie um programa que vai ler varios numeros e colocar em uma lista
#Depois disso crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados respectivamente
#Mostre o conteudo das 3 listas

lista = []
listaPares = []
listaImpares = []

while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    resposta = str(input('Deseja continuar? (S/N): ')).upper().strip()
    while resposta not in 'SN':
        resposta = str(input('Comando invalido. Deseja continuar? (S/N): ')).upper().strip()
    if resposta == 'N':
        break

for num in lista:
    if num % 2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)

print(f'Lista digitada: {lista}')
print(f'Lista dos pares: {listaPares}')
print(f'Lista dos impares: {listaImpares}')
