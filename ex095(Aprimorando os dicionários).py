print('='*15, 'DESAFIO 95', '='*15)

jogador = {}
gol_total = 0
jogadores = []
pos = 0

while True:
    nome = input('\nNome do jogador: ').strip().title()

    jogador[f"{nome}_partidas"] = input(f'Número de partidas que "{nome}" jogou: ').strip()
    while not jogador[f"{nome}_partidas"].isnumeric():
        print('Digite apenas números.')
        jogador[f"{nome}_partidas"] = input(f'Número de partidas que "{nome}" jogou: ').strip()

    for num in range(1, int(jogador[f"{nome}_partidas"]) + 1):
        jogador[f"{nome}_partida_{num}"] = input(f'    Número de gols na partida {num}: ').strip()
        while not jogador[f"{nome}_partida_{num}"].isnumeric():
            print('    Digite apenas números.')
            jogador[f"{nome}_partida_{num}"] = input(f'    Número de gols na partida {num}: ').strip()
        gol_total += int(jogador[f"{nome}_partida_{num}"])
    jogador[f"{nome}_total"] = gol_total
    gol_total = 0

    jogadores.append(nome)

    continuar = input('Deseja continuar [sim/não]: ').strip().lower()
    while continuar != 'sim' and continuar != 'não':
        print('Opção inválida.')
        continuar = input('Deseja continuar [sim/não]: ').strip().lower()
    if continuar == 'não':
        break

print('\n' + 'NUM  NOME    GOLS      TOTAL' + '\n')
for nome in jogadores:
    pos += 1
    print(pos, end=' | ')
    print(nome, end=' | ')
    if jogador[f"{nome}_partidas"] == '0':
        print('0', end=' ')
    else:
        for num in range(1, int(jogador[f"{nome}_partidas"]) + 1):
            print(jogador[f"{nome}_partida_{num}"], end=' ')
    print(f'| {jogador[f"{nome}_total"]}', end=' |')

while True:
    print('\n\nDigite o nome do jogador para ver suas estatísticas.')
    nome = input('Deseja ver as estatísticas de qual jogador [0 para sair]: ').strip().title()
    while nome.isnumeric():
        print('Digite apenas palavras.')
        nome = input('Deseja ver as estatísticas de qual jogador [0 para sair]: ').strip().title()
    while nome in jogadores is False:
        print('Jogador não encontrado.')
    if nome == '0':
        break

    if jogador[f"{nome}_partidas"] == '0':
        print(f'O jogador {nome} não jogou nenhuma partida.')
    else:
        for num in range(1, int(jogador[f"{nome}_partidas"]) + 1):
            if jogador[f"{nome}_partida_{num}"] == '1':
                print(f'   Na partida {num}, {nome} fez 1 gol.')
            elif jogador[f"{nome}_partida_{num}"] == '0':
                print(f'   Na partida {num}, {nome} não fez gol.')
            else:
                print(f'   Na partida {num}, {nome} fez {jogador[f"{nome}_partida_{num}"]} gols.')
