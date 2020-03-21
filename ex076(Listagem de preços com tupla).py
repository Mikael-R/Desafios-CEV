print('='*15, 'DESAFIO 76', '='*15 + '\n')
lista = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '3.75', 'Transferidor', '5.00', 'Estojo', '10.00')  # 0, 9
print('-'*42 + '\n           LISTAGEM DE PREÇOS\n' + '-'*42)
for produto in range(0, 9, 2):
    print(f'{lista[produto]:.<30} R${lista[produto-9]:>7}')
print('-'*42)
