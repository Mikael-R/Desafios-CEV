print('='*15, 'DESAFIO 102', '='*15 + '\n')

def fatorial(num, show=False):
    """<Mostra o fatorial de um número>
    :param num: O número que será calculado.
    :param show: Mostrar, ou não, os cálculos (opcional).
    :return: Retorna o fatorial de num."""
        
    factorial = 1
    for cont in range(num, 0, -1):
        factorial *= cont
        if show:
            if cont > 1:
                print(f'{cont} x ', end='')
            else:
                print(f'{cont} = ', end='')
    return factorial


print(fatorial(5, True))
help(fatorial)
