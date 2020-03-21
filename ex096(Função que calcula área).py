print('='*15, 'DESAFIO 96', '='*15 + '\n')
def area(lar, com):
    mult = lar * com
    print(f'A área de um terreno com {lar:.2f}x{com:.2f} é de {mult:.2f}m²')


largura = float(input('Largura (m): '))

comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)
