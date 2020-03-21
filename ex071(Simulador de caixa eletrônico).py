print('='*15, 'DESAFIO 71', '='*15)
opcoes_saque = ('''
---------- OPÇÕES ----------
[1] 5 reais    [4] 50 reais
[2] 10 reais   [5] 100 reais
[3] 20 reais   [6] Subtrair
----------------------------''')
opcoes_subtracao = ('''
----- OPÇÕES_SUBTRAÇÃO -----
[1] 5 reais    [4] 50 reais
[2] 10 reais   [5] 100 reais
[3] 20 reais
----------------------------''')
dinheiro = 0
subtracao = 0

while True:
    print(opcoes_saque)

    opcao = str(input('\nOpção: ')).strip()
    while opcao not in '123456':
        opcao = str(input('Digite uma opção válida.\nOpção: ')).strip()
    while opcao == '6' and dinheiro == 0:
        opcao = str(input('Não há nenhum valor a ser subtraído.\n\nOpção: ')).strip()

    if opcao == '1':
        dinheiro += 5
    if opcao == '2':
        dinheiro += 10
    if opcao == '3':
        dinheiro += 20
    if opcao == '4':
        dinheiro += 50
    if opcao == '5':
        dinheiro += 100
    if opcao == '6':
        while True:
            print(opcoes_subtracao)

            opcao_subtracao = str(input('\nQuanto deseja subtrair: '))
            while opcao_subtracao not in '12345':
                opcao_subtracao = str(input('Digite uma opção válida.\n\nQuanto deseja subtrair: ')).strip()

            if opcao_subtracao == '1':
                subtracao += 5
            if opcao_subtracao == '2':
                subtracao += 10
            if opcao_subtracao == '3':
                subtracao += 20
            if opcao_subtracao == '4':
                subtracao += 50
            if opcao_subtracao == '5':
                subtracao += 100
            if dinheiro - subtracao == 0:
                print('O valor de saque foi reduzido a zero.\nOperação cancelada.\n')
                subtracao = 0
                break
            if dinheiro - subtracao < 0:
                print('O valor a ser diminuido é maior que o valor a ser sacado.\nOperação cancelada.\n')
                subtracao = 0
                break
            print(dinheiro, subtracao)
            print(f'R${subtracao} foram diminuidos.\n')

    print(f'Valor a ser sacado R${dinheiro - subtracao}')

    sair = str(input('Deseja sacar agora [sim/não]: ')).strip().lower()
    while sair != 'não' and sair != 'sim':
        sair = str(input('Digite corretamente.\nDeseja sacar agora [sim/não]: ')).strip().lower()
    if sair == 'sim':
        break

print('\n' + '='*16 + '\n' + '     SAQUE' + '\n' + '='*16)
# cédulas de 100 reais
nota_100 = dinheiro // 100
dinheiro = dinheiro - nota_100 * 100
if nota_100 > 1:
    print(f'{nota_100} cédulas de R$100')
if nota_100 == 1:
    print(f'1 cédula de R$100')

# cédulas de 50 reais
nota_50 = dinheiro // 50
dinheiro = dinheiro - nota_50 * 50
if nota_50 > 1:
    print(f'{nota_50} cédulas de R$50')
if nota_50 == 1:
    print(f'1 cédula de R$50')

# cédulas de 20 reais
nota_20 = dinheiro // 20
dinheiro = dinheiro - nota_20 * 20
if nota_20 > 1:
    print(f'{nota_20} cédulas de R$20')
if nota_20 == 1:
    print(f'1 cédula de R$20')

# cédulas de 10 reais
nota_10 = dinheiro // 10
dinheiro = dinheiro - nota_10 * 10
if nota_10 > 1:
    print(f'{nota_10} cédulas de R$10')
if nota_10 == 1:
    print(f'1 cédula de R$10')

# cédulas de 5 reais
nota_5 = dinheiro // 5
dinheiro = dinheiro - nota_5 * 5
if nota_5 > 1:
    print(f'{nota_5} cédulas de R$5')
if nota_5 == 1:
    print(f'1 cédula de R$5')
