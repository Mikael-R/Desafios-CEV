print('='*15, 'DESAFIO 87', '='*15 + '\n')
matriz = [[],[],[]]
soma = 0
for l in range(0,3):
        for c in range(0,3):
                matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
                if matriz[l][c] % 2 == 0:
                  soma += matriz[l][c]
print('-'*30)
for l in range(0,3):
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
        print()
matriz_terceira_coluna = [matriz[0][2], matriz[1][2], matriz[2][2]]
matriz_segunda_linha = [matriz[1][0], matriz[1][1], matriz[1][2]]
print('-'*30)
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terçeira coluna é {sum(matriz_terceira_coluna)}')
print(f'O maior valor da segunda linha é {max(matriz_segunda_linha)}')
