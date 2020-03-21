print('='*15, 'DESAFIO 51', '='*15, '\n')
pt = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
cálculo = pt + 10 * razão
for c in range(pt, cálculo, razão):
    print(c, end=' → ')
print('FIM', end='')
