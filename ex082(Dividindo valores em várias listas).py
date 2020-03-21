print('='*15, 'DESAFIO 82', '='*15)
lista = []
pares = []
impares = []
while True:
    num = int(input('\nInforme um número: '))
   
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    continuar = str(input('Deseja continuar [sim/não]: ')).strip().lower()
    while continuar != 'sim' and continuar != 'não':
        print('Digite corretamente.')
        continuar = str(input('\nDeseja continuar [sim/não]: ')).strip().lower()
    if continuar == 'não':      
        break

print(f'\nA lista completa de números é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
