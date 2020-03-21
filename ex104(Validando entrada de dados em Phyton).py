print('='*15, 'DESAFIO 104', '='*15 + '\n')

def leiaInt(msg):
    """Faz um input de um número inteiro. 
    :param return: Retorna um número inteiro"""
    n = input(msg)
    n1 = n.replace('-', '')
    n2 = n.replace('+', '')
    while not n1.isnumeric() and not n2.isnumeric():
        print('ERRO. Digite apenas números inteiros.')
        n = input(msg)
        n1 = n.replace('-', '')
        n2 = n.replace('+', '')
    return int(n)

numero = leiaInt('Digite um número: ')
print(f'Foi digitado o número {numero}')
