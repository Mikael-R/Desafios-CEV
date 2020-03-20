print('='*15, '\033[4mDESAFIO 34\033[m', '='*15, '\n')
print('Lembre-se:\n*Superior a R$1250.00 terão um aumento de 10%.\n*Inferiores ou iguais a R$1250.00 aumento de 15%.\n')
salario = float(input('Valor do salário: R$'))
if salario > 1250 == True:
    print('R${:.2f} com o aumento de 10%.'.format(salario + ((salario * 10) / 100)))
else:
    print('R${:.2f} com o aumento de 10%.'.format(salario + ((salario * 15) / 100)))
