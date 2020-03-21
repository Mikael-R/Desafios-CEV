print('='*15, 'DESAFIO 59', '='*15, '\n')
from time import sleep
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
print('''
--------- Opções ---------
   [1] Somar
   [2] Multiplicar
   [3] Maior número
   [4] Novos números
   [5] Sair do programa
--------------------------''')
opcao = str(input('>>>> Sua opção: ')).strip()
while opcao != 0:
    if opcao == '1':
        print('\n{} + {} = {}'.format(p1, p2, p1 + p2))
    if opcao == '2':
        print('{} x {} = {}'.format(p1, p2, p1 * p2))
    if opcao == '3':
        if p1 > p2:
            print('Entre {} e {} o maior é {}.'.format(p1, p2, p1))
        if p2 > p1:
            print('Entre {} e {} o maior é {}.'.format(p1, p2, p2))
        else:
            print('Os números tem os mesmos valores.')
    if opcao == '4':
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    if opcao == '5':
        print('\nFinalizando...')
        sleep(2)
        print('Programa finalizado. Volte sempre!')
        exit()
    if opcao not in '12345':
        print('Opção inválida! Tente novamente.')
    print('''
--------- Opções ---------
   [1] Somar
   [2] Multiplicar
   [3] Maior número
   [4] Novos números
   [5] Sair do programa
--------------------------''')
    opcao = str(input('>>>> Sua opção: ')).strip()
