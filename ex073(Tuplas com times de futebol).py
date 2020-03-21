print('='*15, 'DESAFIO 73', '='*15 + '\n')
tabela = ('Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Corinthians', 'Internacional', 'Grêmio', 'Bahia',
          'Athletico Paranaense', 'Goiás', 'Vasco da Gama', 'Atlético', 'Botafogo', 'Fortaleza', 'Ceará SC',
          'Fluminense', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('>>> Os cinco primeiros times são: ', end='')
for cinco in range(0, 5):
    if cinco == 3:
        print(f'{tabela[cinco]}', end=' e ')
    if cinco == 4:
        print(f'{tabela[cinco]}', end='.')
    if cinco != 3 and cinco != 4:
        print(f'{tabela[cinco]}', end=', ')
print('')
print('\n>>> Os quatro últimos colocados são: ', end='')
for quatro in range(-4, 0):
    if quatro == -2:
        print(f'{tabela[quatro]}', end=' e ')
    if quatro == -1:
        print(f'{tabela[quatro]}', end='.')
    if quatro != -2 and quatro != -1:
        print(f'{tabela[quatro]}', end=', ')
print('')
print(f'\n>>> Os times em ordem alfabética é:\n{sorted(tabela)}')
print('')
print(f'>>> O time Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição!')
