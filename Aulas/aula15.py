#Funcoes (Parte 1)
#FUncoes sao rotinas, servem como reutilizacao de codigo
#Funcoes sao definidas com o comando def
def soma(a, b):
    print(f'Valor de A = {a}, Valor de B = {b}')
    soma = a + b
    print(f'A soma de {a} + {b} = {soma}')


#*num Pega quantos parametros o usuario digitar
#Retorna uma tupla, é possivel fazer tudo oq é possivel com tuplas
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


#Recebe uma lista como parametro e dobra os valores dela
def dobraLista(lista):
    for i in range(0, len(lista)):
        lista[i] = lista[i] * 2
    print(lista)


#Programa Principal
soma(3, 8)
#Posso especificar a ordem dos parametros explicitamente
soma(b=3, a=8)

#Passo os parametros para a funcao contador
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#Passa a lista valores para a funcao dobraLista
valores = [7, 7, 4, 2, 3]
dobraLista(valores)
