#Faça um programa que leia uma frase pelo teclado e mostre
#Quantas vezes aparece a letra "a"
#Em que posicao ela aparece a primeira vez
#Em que posicao ela aparece a ultima vez

frase = str(input('Digite uma frase quealquer: ')).lower().strip()
print(f'A sua frase tem {frase.count('a')} letras a')
print(f'A primeira letra a esta na posicao {frase.find('a') + 1}')
print(f'A ultima letra a esta na posicao {frase.rfind('a') + 1}')
