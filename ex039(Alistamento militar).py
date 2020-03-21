print('='*15, 'DESAFIO 39', '='*15, '\n')
print('_'*32, '\nLembre-se:\nO alistamento é feito com 18 anos.\n' + '_'*32, '\n')
from datetime import datetime
nascimento = int(input('Ano de nascimento: '))
ano = datetime.now()
idade = ano.year - nascimento
alistamento = nascimento + 18
print('\nEssa pessoa tem {} anos.'.format(idade))
if idade < 18:
    daqui = 18 - idade
    print('Deverá se alistar em {} daqui a {} anos.'.format(alistamento, daqui))
elif idade == 18:
    print('Deverá se alistar imediatamente.')
elif idade > 18:
    daqui = idade - 18
    print('Deveria ter se alistado em {} a {} anos atrás.'.format(alistamento, daqui))
