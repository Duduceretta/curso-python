#Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera adicionado
#No final serao exibidos todos os valores unicos digitados em ordem crescente

valoresDigitados = []

while True:
    numero = int(input('Digite um numero: '))
    if numero not in valoresDigitados:
        valoresDigitados.append(numero)
        print('Numero adicionado com sucesso')
    else:
        print('Numero ja foi adicionado')

    reposta = str(input('Deseja continuar? (S/N): ')).strip().upper()
    while reposta not in 'SN':
        reposta = str(input('Codigo invalido. Deseja continuar? (S/N): ')).strip().upper()
    if reposta == 'N':
        break

print(f'Os valores adicionados foram: {valoresDigitados}')
valoresOrdenados = valoresDigitados[:]
valoresOrdenados.sort()
print(f'Valores ordenados crescentemente: {valoresOrdenados}')
