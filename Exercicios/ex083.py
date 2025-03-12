#Crie um programa onde o usuario digite uma expressao qualquer que use parenteses. Seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta

expressao = str(input('Digite a expressao: ')).strip()
contaParentesesEsq = 0
contaParentesesDir = 0

for i in range(0, len(expressao)): 
    if expressao[i] == '(':
        contaParentesesEsq += 1
    elif expressao[i] == ')':
        contaParentesesDir += 1

if contaParentesesDir == contaParentesesEsq:
    print('A sua expressao é valida!')
else:
    print('A sua expressao nao é valida!')