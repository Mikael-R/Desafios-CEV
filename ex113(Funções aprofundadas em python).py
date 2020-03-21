print('='*15, 'DESAFIO 113', '='*15)


def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('ERRO. Digite apenas números inteiros.')
            continue
        except KeyboardInterrupt:
            print('Nenhum número foi digitado.')
            return None
        else:
            return num


def leiaFloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('ERRO. Digite apenas números reais.')
            continue
        except KeyboardInterrupt:
            print('Nenhum número foi digitado.')
            return None
        else:
            return num


num_inteiro = leiaInt('\nDigite um número inteiro: ')
num_real = leiaFloat('\nDigite um número real: ')
print(f'Inteiro: {num_inteiro}\nReal: {num_real}')
