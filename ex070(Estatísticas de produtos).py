print('='*15, 'DESAFIO 70', '='*15, '\n')
print('-'*26+'\n    LOJA SUPER BARATÃO     \n'+'-'*26)
total = cont_1000 = cont = 0
while True:
    produto_nome = str(input('\nNome do produto: ')).lower().strip()
    produto_preco = float(input('Preço do produto: R$'))
    total += produto_preco
    if produto_preco > 1000:
        cont_1000 += 1
    cont += 1
    if cont == 1:
        caro_preco = produto_preco
        caro_nome = produto_nome
    else:
        if produto_preco > caro_preco:
            caro_preco = produto_preco
            caro_nome = produto_nome
    continuar = str(input('Deseja cadastrar mais um produto [sim/não]? ')).strip().lower()
    while continuar != 'sim' and continuar != 'não':
        continuar = str(input('Deseja cadastrar mais um produto [sim/não]? ')).strip().lower()
    if continuar == 'não':
        break
print('\n'+'-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'O total da compra foi de R${total:.2f} na loja.')
if cont_1000 > 1:
    print(f'{cont_1000} produtos custão mais de R$1000.00 na loja.')
if cont_1000 == 1:
    print('1 produto custa mais de R$1000.00 na loja.')
if cont_1000 == 0:
    print('Nenhum produto custa mais de R$1000.00 na loja.')
print(f'O produto mais caro: {caro_nome}\nO produto mais caro custa: R${caro_preco:.2f}')
