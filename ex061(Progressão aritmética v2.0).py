print('='*15, 'DESAFIO 61', '='*15, '\n')
print('-'*15+'\nGERADOR DE PA V2.0\n'+'-'*15+'\n')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
print('')
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
