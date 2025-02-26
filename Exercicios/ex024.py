#Crie um programa para saber se o nome da cidade começa ou nao com a palavra SANTO

cidade = str(input('Digite o nome da sua cidade: ')).strip().lower()
cidadeSplitada = cidade.split()
print(f'Sua cidade comeca com Santo?: {cidadeSplitada[0] == 'santo'}')