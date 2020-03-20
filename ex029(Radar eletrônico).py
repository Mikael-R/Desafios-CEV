print('='*15, 'DESAFIO 29', '='*15, '\n')
velocidade = float(input('Velocidade do veículo em km: '))
if velocidade>80:
    print('Você foi multado por ultrapassar o limite de 80km/h! E devará pagar R${:.2f} de multa!'.format(velocidade*7))
