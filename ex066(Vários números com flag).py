print('='*15, 'DESAFIO 66', '='*15, '\n')
cont = soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'\nForam digitados {cont} números e a soma entre eles é {soma}.')
