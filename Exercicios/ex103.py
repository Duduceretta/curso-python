#Faça um programa que tenha uma funcao chamada ficha que receba dois parametros opcionais: o nome de um jogador e qtos gols ele marcou
#O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente

def ficha(n = '<desconhecido>', g = 0):
    return f'O jogador(a) {n} fez {g} gol(s) no campeonato'


#Programa principal
nome = input('Digite o nome do jogador: ').strip()
gols = input('Numero de gols: ').strip()

if gols.isdigit():  
    gols = int(gols)  # Converte para inteiro
else:
    gols = 0  # Se não for um número, assume 0

# Verifica se o nome foi digitado corretamente
if not nome:  
    nome = '<desconhecido>'

# Chama a função e exibe o resultado
print(ficha())
