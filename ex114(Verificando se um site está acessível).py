print('='*15, 'DESAFIO 114', '='*15)

from urllib.error import URLError
from urllib.request import urlopen as open


def acessarSite(url):
    try:
        open('https://www.google.com.br')
    except:
        print('Não há internet.')
        exit()
    try:
        open(url)
    except ValueError:
        print('O site é inválido')
    except URLError:
        print('O site não é acessível ou não existe.')
    else:
        print('O site está acessível.')


print('\nExemplo: https://www.google.com.br')
acessarSite(input('\nUrl: '))
