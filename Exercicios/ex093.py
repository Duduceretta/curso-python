#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador, e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
#No final tudo isso sera guardado em um dicionario, incluindo o total de gols feitos durante o campeonato

jogador = {}
listaGols = []
totalGols = 0

jogador['nome'] = str(input('Nome: ')).strip()
jogador['partidasJogadas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

for i in range(0, jogador['partidasJogadas']):
    listaGols.append(int(input(f'Quantos gols na partida {i + 1}?: ')))
    totalGols += listaGols[i]

jogador['gols'] = listaGols[:]
jogador['totalGols'] = totalGols

print('-=' * 20)
for key, value in jogador.items():
    print(f'O campo {key} tem valor {value}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidasJogadas"]} partidas')

for i in range(0, jogador['partidasJogadas']):
    print(f'  => Na partida {i + 1}, fez {listaGols[i]} gols')
print(f'Foi um total de {jogador["totalGols"]} gols.')
