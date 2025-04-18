#Tratamento de erros e excecoes

try:
    #Tenta executar as linhas
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Nao e possivel dividir por zero')
except KeyboardInterrupt:
    print('O usuario preferiu nao inserir os dados')
except Exception as erro:
    #Mostra a classe do erro
    print(f'Problema encontrado foi {erro.__class__}')
    #caso der erro mostra uma excecao 
    print(f'Infelizmente tivemos um problema :(')
else:
    #caso nao der problema
    print(f'O resultado e {r:.2f}')
finally:
    #Ocorre independente se tiver falha ou nao
    print('Volte sempre, Muito Obrigado!')