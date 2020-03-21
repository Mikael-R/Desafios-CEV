print('='*15, 'DESAFIO 67', '='*15, '\n')
while True:
    num = int(input('\n[Valor negativo para sair]\nInforme um número para ver sua tabuada: '))
    if num < 0:
        print('Programa encerrado, volte sempre!')
        break
    print('-' * 15)
    for m in range(1, 11):
        print(f'{num} x {m} = {num * m}')
    print('-' * 15)
