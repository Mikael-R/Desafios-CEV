print('='*15, 'DESAFIO 62', '='*15, '\n')
print('-'*15+'\nGERADOR DE PA V3.0\n'+'-'*15+'\n')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
print('')
cont = 10
termos = 0
while cont > 0:
    print('{} → '.format(primeiro), end='')
    primeiro += razao
    cont -= 1
    termos += 1
    if cont == 0:
        cont = int(input('PAUSA\nAcrescentar mais números na sequência: '))
print('\nPA finalizada, foram mostrados {} termos.'.format(termos))
