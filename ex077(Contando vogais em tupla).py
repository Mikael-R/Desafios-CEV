print('='*15, 'DESAFIO 77', '='*15 + '\n')
palavras = ('teste', 'programar', 'futuro', 'estudar', 'empresário',
            'rico', 'brilhante', 'pensar', 'felicidade', 'computador')
for p in palavras:  # Verifica cada palavra
    print(f'A palavra {p.upper()} tem as vogais ', end='')
    for l in p:  # Verifica cada letra da palavra
        if l in 'aeiou':
            print(l, end=' ')
    print('')
