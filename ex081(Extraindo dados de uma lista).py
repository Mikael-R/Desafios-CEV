print('='*15, 'DESAFIO 81', '='*15)
lista = []
cont = 0
while True:
    num = int(input('\nDigite um número: '))
    cont += 1
    lista.append(num)
    continuar = str(input('Deseja continuar [sim/não]: ')).strip().lower()
    while continuar != 'sim' and continuar != 'não':
        print('Digite corretamente.')
        continuar = str(input('\nDeseja continuar [sim/não]: ')).strip().lower()
    if continuar == 'não':
        break
if cont == 1:
    print('\nFoi digitado apenas 1 número.')
else:
    print(f'\nForam digitados {cont} números.')
    print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
if '5' in 'lista':
    print(f'O número 5 foi digitado na lista')
else:
    print('O número 5 não foi digitado na lista.')
