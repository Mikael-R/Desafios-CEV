print('='*15, 'DESAFIO 75', '='*15 + '\n')
numeros = tuple(int(input('Informe um número: '))for c in range(4))
print(f'\nO número 7 apareceu {numeros.count(7)} vez(s).')
if 3 in numeros:
    print(f'O primeiro número 3 está na {numeros.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print('Os números pares digitados foram: ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end='  ')
