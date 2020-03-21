print('='*15, 'DESAFIO 103', '='*15 + '\n')

def ficha(jogador, gol):
    if jogador == '':
        jogador = '<desconhecido>'
    if gol == '':
        gol = '<0>'
    print(f'O jogador {jogador} fez {gol} gol(s).')


nome = input('Nome do jogador: ').strip().title()
gols = input('Número de gols: ').strip()

ficha(nome, gols)
