#Faça um programa que tenha uma funcao notas que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informacoes
#Quantidade de notas
#Maiopr e menor nota
#Media da turma
#Situacao opcional


def recebeNotas(*notas, sit = False):
    """Recebe varias notas de alunos e analisa esses dados
    Args:
        sit (bool, optional): Diz conforme a media a situacao (Boa, Razoavel, Ruim). Defaults to False.
    Returns:
        dict: Dicionario com o numero de notas, maior e menor nota, e a media da turma
    """
    dicionario = {}
    dicionario['total'] = len(notas)
    dicionario['maior'] = max(notas)
    dicionario['menor'] = min(notas)
    dicionario['media'] = sum(notas) / len(notas)
    if sit:
        if dicionario['media'] > 7:
            dicionario['situacao'] = 'Boa'
        elif dicionario['media'] > 5:
            dicionario['situacao'] = 'Razoavel'
        else:
            dicionario['situacao'] = 'Ruim'
    return dicionario

#Programa Princpal
resp = recebeNotas(3.5, 2, 6.5, 2, 7, 4, sit = True) 
print(resp)
