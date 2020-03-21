print('='*15, 'DESAFIO 40', '='*15, '\n')
print('Lembre-se:\n-Média 5.0 ou menos: REPROVADO\n-Média entre 5.0 e 6.9: RECUPERAÇÃO\n-Média 7.0 acima: APROVADO\n')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terçeira nota: '))
n4 = float(input('Quarta nota:'))
media = (n1 + n2 + n3) / 3
if media < 5.0:
    print('\nMédia: {:.1f}\nResultado: \033[31mREPROVADO\033[m!'.format(media))
elif media < 7.0:
    precisa = 7 - media
    print('\nMédia: {:.1f}\nResultado: \033[33mRECUPERAÇÃO\033[m!\nPrecisa: {:.1f}'.format(media, precisa))
elif media >= 7.0:
    print('\nMédia: {:.1f}\nResultado: \033[32mAPROVADO\033[m!'.format(media))
