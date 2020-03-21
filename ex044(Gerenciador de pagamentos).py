print('='*15, 'DESAFIO 44', '='*15, '\n')
preco = float(input('Preço das compras: R$'))
print('''
Escolha um dos métodos de pagamento:
_____________________________________________
[1] A vista dinheiro/cheque: 10% de desconto|
[2] A vista no cartão: 5% de desconto       |
[3] Em até 2x no cartão: preço normal       |
[4] 3x ou mais no cartão: 20% de juros      |    
____________________________________________|
''')
opcao = int(input('Opção de pagamento: '))
if opcao == 1:
    desconto = (preco * 10) / 100
    print('A compra de R${:.2f} custará R${:.2f} no final.'.format(preco, preco - desconto))
elif opcao == 2:
    desconto = (preco * 5) / 100
    print('A compra de R${:.2f} custará R${:.2f} no final.'.format(preco, preco - desconto))
elif opcao == 3:
    parcelas = int(input('Número de parcelas: '))
    pagamento = preco / parcelas
    if parcelas > 2:
        print('\033[31mO número máximo de parcelas da opção [2] são duas!\033[m')
    else:
        print('A compra de R${:.2f} será parcelada em {}x de R${:.2f} sem juros.'.format(preco, parcelas, pagamento))
elif opcao == 4:
    parcelas = int(input('Número de parcelas: '))
    juros = (preco * 20) / 100
    preco_parcelas = (preco + juros) / parcelas
    if parcelas < 3:
        print('\033[31mO número mínimo de parcelas da opção [4] são três!\033[m')
    else:
        print('A compra de R${:.2f} custará R${:.2f} e será parcelada'
              ' em {}x de R${:.2f}'.format(preco, preco + juros, parcelas, preco_parcelas))
else:
    print('\033[1;31mOpção inválida!\033[m')
