num = int(input('Digite um número: '))
primo = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        primo += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\n\033[mO número {} foi divisível {} vezes.'.format(num, primo), end='')
if primo >= 2:
    print(' Portanto ele \033[32mé primo!')
else:
    print(' Portanto ele \033[31mnão é primo!')
