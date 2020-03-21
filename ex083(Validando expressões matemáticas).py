print('='*15, 'DESAFIO 83', '='*15 + '\n')

expressao = str(input('Digite a expressão: '))
cont_1 = expressao.count('(')
cont_2 = expressao.count(')')

if cont_1 == cont_2:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
