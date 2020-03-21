print('='*20, 'DESAFIO 20', '='*20)
print('')
from random import shuffle
p1 = input('Pessoa 1: ')
p2 = input('Pessoa 2: ')
p3 = input('Pessoa 3: ')
p4 = input('Pessoa 4: ')
lista = [p1, p2, p3, p4]
liran = shuffle(lista)
print('A ordem será: ')
print(lista)
