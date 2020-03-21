print('='*15, 'DESAFIO 55', '='*15, '\n')
pesos = [float(input('Informe o peso da {}ª pessoa: '.format(c))) for c in range(1, 6)]
print('Maior peso: {:.1f}'.format(max(pesos)))
print('Menor peso: {:.1f}'.format(min(pesos)))
