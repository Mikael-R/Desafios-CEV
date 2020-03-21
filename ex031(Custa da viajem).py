print('='*15, 'DESAFIO 31', '='*15, '\n')
print('-'*25, '\nLembre-se:\nR$0,50 por Km para viagens de até 200km.\nR$0,45 para viagens mais longas.\n', '-'*25)
distancia = int(input('Distância da viagem em Km: '))
if distancia>200:
    print('O preço da passagem será R${:.2f}'.format(distancia * 0.45))
else:
    print('O preço da passagem será R${:.2f}'.format(distancia * 0.50))
