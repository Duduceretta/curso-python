#Dicionarios
#Dicionarios sao declarados por {}
pessoas = {'nome': 'Eduardo', 'sexo': 'M', 'idade': 20} #ou pessoas = dict()
print(pessoas)
#Deleta a chave nome
#del pessoas['nome']

#Mostra o valor da chave nome
print(pessoas['nome'])
#Mostra o valor da chave idade
print(pessoas['idade'])
#Referencia de dicionario em f-strings
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#Mostra todas as chaves (nome, sexo e idade) do dicionario
print(pessoas.keys())
#Mostra todos os valores (Eduardo, M, 20) do dicionario
print(pessoas.values())
#Mostra todos os elementos (chave: valor) do dicionario
print(pessoas.items())
#Adiciona outra chave e valor ao dicionario
pessoas['peso'] = 98
#Mostra a chave e o valor
for key, valor in pessoas.items():
    print(f'{key} = {valor}')

#Dicionarios dentro de listas
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

print(f'{"Mostrando os estados do brasil":^40}')
for estado in brasil:
    print(estado)

#Mostra a uf do estado guardado na posicao 0 da lista brasil
print(brasil[0]['uf'])

estado = {}
brasil2 = []

#Lendo dados e armazenando na lista brasil2
for i in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil2.append(estado.copy())

for estado in brasil2:
    for key, value in estado.items():
        print(f'O campo {key} tem valor {value}')
