print('='*15, 'DESAFIO 47', '='*15 + '\n')
num = int(input('Informe um número: '))
print('Os pares que estão entre 1 e {} são:'.format(num), end=' ')
for c in range(2, num +2, 2):
    print(c, end=' ')
