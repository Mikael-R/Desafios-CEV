print('='*15, 'DESAFIO 46', '='*15, '\n')
from time import sleep
num = int(input('Digite o valor da contagem: '))
for c in range(num , 0, -1):
    print(c)
    sleep(1)
print('KABOM!')
