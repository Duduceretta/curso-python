#Refaça o ex051 lendo o primeiro termo e a razao de uma PA mostrando os 10 primeiros termos da progressao usando while

print('======10 Primeiro Termos da PA======')
primeiroTermo = int(input('Qual o primeiro termo da PA?: '))
razao = int(input('Qual a razao da PA?: '))
i = 1
print('Os 10 primeiros termos sao: ') 
while i < 11:
    print(f'{primeiroTermo}', end=' -> ')
    primeiroTermo = primeiroTermo + razao
    i = i + 1
print('ACABOU')
