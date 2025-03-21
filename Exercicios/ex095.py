#Aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

dadosJogador = {}
jogadores = []
gols = []
totalGols = 0

while True:
    print('-=' * 20)
    dadosJogador['nome'] = str(input('Nome: ')).strip()
    dadosJogador['partidasJogadas'] = int(input(f'Quantas partidas {dadosJogador['nome']} jogou?: '))
    for i in range(0, dadosJogador['partidasJogadas']):
        gols.append(int(input(f'Quantos gols na partida {i+1}?: ')))
        totalGols += gols[i]
    dadosJogador['gols'] = gols[:]
    dadosJogador['totalGols'] = totalGols
    gols.clear()
    totalGols = 0
    jogadores.append(dadosJogador.copy())

    resposta = str(input('Deseja continuar? (S/N): ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Comando invalido. Deseja continuar? (S/N): ')).strip().upper()

    if resposta == 'N':
        break

print('-=' * 30)
print(f'{"cod":<3} {"nome":<10}{"gols":<15}{"total":>9}')
print('--' * 30)
for i, dicionario in enumerate(jogadores):
    print(f'{i:>3} {dicionario['nome']:<10}{dicionario['gols']!s:<15}{dicionario['totalGols']:>8}')

while True:
    print('--' * 30)
    busca = int(input('Mostrar dados de queal jogador? (999 para parar): '))
    if busca == 999:
        break

    if 0 <= busca < len(jogadores):
        print(f'-- Levantamento do jogador {jogadores[busca]['nome']}: ')
        for i, gols in enumerate(jogadores[busca]['gols']):
            print(f'  -> No jogo {i + 1} fez {gols} gols')
    else:
        print('Jogador nao encontrado')    
print('-=' * 15, ' >>> FIM DO PROGRAMA <<< ', '=-' * 15)
