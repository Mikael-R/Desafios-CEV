print('=' * 15, 'DESAFIO 32', '=' * 15, '\n')
from datetime import datetime
ano = int(input('Informe um ano, -1 é o ano atual: '))
if ano == -1:
    ano = datetime.now().year
if ano % 4 == 0 and ano % 100 and ano % 400 != 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
