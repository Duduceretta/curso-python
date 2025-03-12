#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastra-os ja na posicao correta de insercao (sem usar o sort())
#No final mostra a lista ordenada na tela

listaOrdenada = []

for i in range(5):
    numero = int(input('Digite um numero: '))
    if i == 0 or numero > listaOrdenada[-1]:
        listaOrdenada.append(numero)
        print('Numero adicionado ao final da lista...')
    else:
        for pos, i in enumerate(listaOrdenada):
            if numero <= listaOrdenada[pos]:
                listaOrdenada.insert(pos, numero)
                print(f'Numero adicionado na posicao {pos} da lista...')
                break 
print(f'Os valores digitados na ordem sao: {listaOrdenada}')
