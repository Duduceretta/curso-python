#Listas (parte 2)
#Listas dentro de listas

teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
#Adiciona o gustavo e a idade na lista
galera.append(teste.copy()) #Ou teste[:]
#Muda a lista teste
teste[0] = 'Maria'
teste[1] = 19
#Adiciona a Maria e a idade na lista galera
galera.append(teste[:])
print(galera)

pessoas = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas)
#Mostra ['Joao', 19]
print(pessoas[0])
#Mostra Joao
print(pessoas[0][0])

#Mostra cada lista dentro da lista pessoas
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos de idade')

#Mostra somente os nomes
for p in pessoas:
    print(p[0])

#Mostra somente as idades
for p in pessoas:
    print(p[1])

lista = []
dados = []
for i in range(0, 3):
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    #Faz a copia da lista dados na estrutura lista
    lista.append(dados[:])
    #Limpa a lista dados
    dados.clear()

print(lista)

#Verifica quais pessoas tem mais de 20 anos
for p in lista:
    if p[1] >= 20:
        print(f'A pessoa {p[0]} tem mais de 20 anos')
