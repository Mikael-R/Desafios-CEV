print('='*15, 'DESAFIO 93', '='*15 + '\n')

jogador = {}
gol_total = 0

jogador["nome"] = input('Nome do jogador: ').strip()

jogador["partidas"] = input(f'\nNúmero de partidas que "{jogador["nome"]}" jogou: ').strip()
while not jogador["partidas"].isnumeric():
    print('Digite apenas números.')
    jogador["partidas"] = input(f'Número de partidas que "{jogador["nome"]}" jogou: ').strip()

for num in range(1, int(jogador["partidas"]) + 1):
    jogador[f"gol_partida_{num}"] = input(f'    Número de gols na partida {num}: ').strip()
    while not jogador[f"gol_partida_{num}"].isnumeric():
        print('    Digite apenas números.')
        jogador[f"gol_partida_{num}"] = input(f'    Número de gols na partida {num}: ').strip()
    gol_total += int(jogador[f"gol_partida_{num}"])

print('__'*10)
print(f'Nome: {jogador["nome"]}')

if int(jogador["partidas"]) < 1:
    print('Partidas: 0')
else:
    print(f'Partidas: {jogador["partidas"]}')
    for num in range(1, int(jogador["partidas"]) + 1):
        print(f'Gols da partida {num}: {jogador[f"gol_partida_{num}"]}')

print(f'Total de gols: {gol_total}')
print('__'*10)
