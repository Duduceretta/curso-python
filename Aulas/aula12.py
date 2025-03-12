#Listas
#Listas podem ser modificadas diferentemenet das tuplas

#Listas sao definidas por colchetes
num = [2,5,9,1,2,4,8]
#Modifica o numero na posicao 2 (9) para 3
num[2] = 3
#Adiciona o elemento ao final de uma lista
num.append(7)
#Adiciona o elemento (0) no indice indicado (2)
num.insert(2, 4)
#Remove o ultimo elemento da lista
num.pop()
#Remove o elemento do indice indicado
num.pop(1)
#Remove a primeira ocorrencia do numero
num.remove(2)
#Verifica se o numero esta na lista e remove a primeira ocorrencia dele
if 4 in num:
    num.remove(4)
else:
    print('O numero nao esta na lista')
#Ordena a lista
#num.sort()
#Ordena a lista de forma decrescente
#num.sort(reverse=True)
#Retorna o total de elementos na lista
print(len(num))
print(num)
print('--' * 20)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for i in range(0,4):
    valores.append(int(input('Digite um numero: ')))

for pos, i in enumerate(valores):
    print(f'Na posicao {pos} encontre o valor {i}!')

#Cria uma ligacao entre as listas, nao uma copia
a = [2,3,5,7]
b = a
#Cria uma copia dos elementos, so altera a lista em b
b = a[:]
#Muda nas duas listas
b[2] = 0
print(f'Lista A: {a}')
print(f'Lista B: {b}')