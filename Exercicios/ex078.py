#Faça um programa que leia 5 valores numericos e guarde numa lista
#No final mostre qual foi o menor e o maior valor digitado e as suas respectivas posicoes na lista

valores = []
menor = 0
maior = 0

for i in range(0,5):
    valores.append(int(input(f'Digite um valor para a posicao {i}: ')))
    if i == 0:
        maior = valores[i]
        menor = valores[i]
    elif valores[i] > maior:
        maior = valores[i]
    elif valores[i] < menor:
        menor = valores[i]
print(f'Os valores digitados foram: {valores}')

print(f'O maior valor digitado foi: {maior} nas posicoes ', end= '')
for pos, i in enumerate(valores):
    if i == maior:
        print(f'{pos}... ', end='')

print(f'\nO menor valor digitado foi: {menor} nas posicoes ', end= '')
for pos, i in enumerate(valores):
    if i == menor:
        print(f'{pos}... ', end='')
