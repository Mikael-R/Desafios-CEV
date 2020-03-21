print('='*15, 'DESAFIO 37', '='*15, '\n')
num = int(input('Informe um  número inteiro: '))
print('''
Escolha uma das bases para a conversão:
____________________
[1] BINÁRIO         |
[2] HEXADECIMAL     |
[3] OCTAL           |
____________________|
''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    binario = bin(num)
    print('O número {} em formato binário é {}'.format(num, binario[2:]))
elif opcao == 2:
    hexadecimal = hex(num)
    print('O número {} em formato hexadecimal é {}'.format(num, hexadecimal[2:]))
elif opcao == 3:
    octal = oct(num)
    print('O número {} em formato octal é {}'.format(num, octal[2:]))
else:
    print('\033[1;31mOpção inválida!\033[m')
