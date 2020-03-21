print('=' * 15, 'DESAFIO 38', '=' * 15, '\n')  # end='' ele desquebra a linha
print('_'*75+'\nLembre-se:\nSe a prestação mensal for maior que 30% do salário o empréstimo será negado.\n'+'_'*75)
casa = float(input('Valor do imóvel: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Anos de prestação: '))
prestacao = casa / (anos * 12)
porcentagem = (salario * 30) / 100
print('A prestação mensal será de R${:.2f} em {} anos.'.format(prestacao, anos))
if prestacao >= porcentagem:
    print('\033[1;31mEmpréstimo negado\033[m!')
else:
    print('\033[1;32mEmpréstimo aprovado\033[m!')
