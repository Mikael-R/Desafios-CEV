soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        contador = contador + c
print('A soma de todos os {} valores ímpares multiplos de 3 até 500 é {}!'.format(contador, soma))
