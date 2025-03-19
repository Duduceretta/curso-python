#Crie um programa onde o usuario possa digitar 7 valores numericos e cadastre-os em um lista unica que mantenha separados os vaolores pares e impares.
#No final mostre os valores pares e impares em ordem crescente

#Usando listas adicionais
'''listaPrincipal = []
listaPares = []
listaImpares = []

for i in  range(7):
    numero = int(input(f'Digite o {i + 1} valor: '))
    if numero % 2 == 0:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)

listaPares.sort()
listaImpares.sort()
listaPrincipal.append(listaPares)
listaPrincipal.append(listaImpares)

print(f'Os valores pares digitado foram: {listaPrincipal[0]}')
print(f'Os valores impares digitado foram: {listaPrincipal[1]}')'''

#Usando somente uma lista
lista = [[], []]

for i in range(7):
    num = int(input(f'Digite o {i + 1}o. numero: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Os valores pares digitado foram: {lista[0]}')
print(f'Os valores impares digitado foram: {lista[1]}')
