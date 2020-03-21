print('='*15, 'DESAFIO 65', '='*15, '\n')
continuar = 'S'
cont = total = 0
while continuar == 'S':
    cont += 1
    num = int(input('Informe um número: '))
    total += num
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if continuar not in 'SN':
        continuar = str(input('Opção inválida. Deseja continuar [S/N]? ')).upper().strip()
    if continuar == 'N':
        break
media = total / cont
if cont == 1:
    print('\nFoi digitado apenas um número.')
    exit()
else:
    print('\nForam digitados {} números e {:.2f} foi a média entre eles.'.format(cont, media))
print('O maior valor é {} e o menor é {}.'.format(maior, menor))
