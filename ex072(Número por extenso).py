print('='*15, 'DESAFIO 73', '='*15 + '\n')
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número [0 a 20]: '))
    if num <= 20:
        if num >= 0:
            break
print(f'\nO número "{num}" escrito por extenso é "{extenso[num]}".')
