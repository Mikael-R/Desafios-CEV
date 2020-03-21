print('='*15, 'DESAFIO 49', '='*15, '\n')
num = int(input('Informe um número e veja tabuada: '))
print('_'*14)
for mult in range(1, 11):
    result = num * mult
    print('{} x {} = {}'.format(num, mult, result))
print('_'*14)
