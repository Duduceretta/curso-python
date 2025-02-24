#Operadores Aritméticos
#
# soma = '+'
# subtracao = '-'
# multiplicacao = '*'
# divisao = '/'
# potenciacao = '**'
# divisao inteira = '//'
# resto da divisao = '%'
#
# Ordem de precedencia das operacoes
#
# 1 = '()'
# 2 = '**'
# 3 = '*', '/', '//' e '%'
# 4 = '+' e '-'

n1 = int(input('Digite um numero: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
potencia = n1 ** n2
print(f'A soma é: {soma}, A subtracao é: {subtracao}, A multiplicacao é: {multiplicacao}, A divisao é: {divisao:.3f}')
print(f'Divisao Inteira: {divisaoInteira}, Potencia: {potencia}')
