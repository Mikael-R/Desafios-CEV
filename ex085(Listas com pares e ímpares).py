print('='*15, 'DESAFIO 85', '='*15 + '\n')
lista = [[], []]
for c in range(1, 8):
    valor = float(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f'\nOs números pares são: {lista[0]}\nOs números ímpares são: {lista[1]}')
