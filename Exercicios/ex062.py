#Melhore o ex061 perguntando para o usuario se ele quer mostrar mais alguns termos O programa encerra quando ele disser que quer mostrar 0 termos 

primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
i = 11
termosMostrados = 10
print('Mostrando os termos da PA: ')
while i > 1:
    print(f'{primeiroTermo}', end=' -> ')
    primeiroTermo = primeiroTermo + razao
    if(i == 2):
        print('Deseja ver mais numeros?')
        print('Digite [0] se quiser sair')
        mostrarMais = int(input('Mais quantos termos voce quer mostrar?: '))
        i = i + mostrarMais 
        termosMostrados = termosMostrados + mostrarMais
    i = i - 1 

print(f'O total de termos mostrados foi {termosMostrados}!')
print('ACABOU')