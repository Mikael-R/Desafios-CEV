def titulo(num=000, saltar=True, simbolo='=', distanciamento=15):
    if saltar == False:
        print(f'{simbolo}'*distanciamento, f'DESAFIO {num}', f'{simbolo}'*distanciamento, end='\n')
    else:
        print(f'{simbolo}'*distanciamento, f'DESAFIO {num}', f'{simbolo}'*distanciamento, end='\n\n')


def leiaDinheiro(txt):
    dinheiro = input(txt).strip().replace(',', '.')
    dinheiro_exame = dinheiro.replace('.', '')
    while not dinheiro_exame.isnumeric() or dinheiro.count('.') > 1:
        print('ERRO: Digite apenas números.')
        dinheiro = input(txt).strip().replace(',', '.')
        dinheiro_exame = dinheiro.replace('.', '')

    return float(dinheiro)
