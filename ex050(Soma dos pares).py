print('='*15, 'DESAFIO 49', '='*15, '\n')
soma = 0
contador = 0
for c in range(1, 7):
    num = int(input('Informe o {}° número: '.format(c)))
    if num % 2 == 0:   
        soma += num
        contador += 1
if contador == 1:
    print('Foi informado 1 número par e seu valor é {}.'.format(soma))
else:
    print('Foi informado {} números pares e a soma deles é {}.'.format(contador, soma))
