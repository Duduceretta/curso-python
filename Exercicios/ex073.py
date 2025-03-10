#Crie uma tupla preenchida com os 20 primeiros colocados do campeonato brasileiro na ordem de colocao, depois mostre
#Apenas os 5 primeiros colocados
#Os ultimos 4 colocados
#Uma lista com os times em ordem alfabetica
#Em que posicao esta o time da chapecoense

times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atletico-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport', 'Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')

print('-=-' * 20)
print(f'Os cinco primeiros colocados sao: {times[0:5]}')
print('-=-' * 20)
print(f'Os ultimos quatro colocados sao: {times[-4:]}')
print('-=-' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=-' * 20)
print(f'A Chapecoense esta na {times.index('Chapecoense') + 1} posicao')
print('-=-' * 20)
