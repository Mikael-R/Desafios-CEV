print('=' * 15, 'DESAFIO 41', '=' * 15, '\n')
print('_' * 22 + "\nLembre-se:\n-Até 9 anos:  Mirim\n-Até 14 anos: Infantil\n-Até 19 anos: Junior\n-Até 20 anos: Sêni"
                 "\n-Acima:       Master\n" + '_' * 22)
from datetime import datetime
ano = datetime.now()
nascimento = int(input('Ano de nascimento: '))
idade = ano.year - nascimento
print('\nO atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classsificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade == 20:
    print('Classificação: Sênior')
elif idade > 20:
    print('Classificação: Master')
