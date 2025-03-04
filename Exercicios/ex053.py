#Faca um programa que leia uma frase qualquer e diga se ele é um palindromo desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().replace(' ', '').lower()
palindromo = ''

for i in range(len(frase) - 1, -1, -1):
    palindromo = palindromo + frase[i]

print('Frase normal')
print(frase)
print('Frase palindromo')
print(palindromo)

if palindromo == frase:
    print('É um palindromo')
else:
    print('Nao sao um palindromo')

