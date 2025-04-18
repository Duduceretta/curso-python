#Crie um codigo em python que teste se o site pudim esta acessivel pelo computador usado

import requests

def verificar_site(url):
    try:
        resposta = requests.get(url, timeout=5)
        if resposta.status_code == 200:
            print(f'Consegui acessar o site do pudim')
    except requests.exceptions.RequestException as erro:
        print(f'Nao consegui acesssar o site do pudim')


verificar_site('https://www.pudim.com.br/')
