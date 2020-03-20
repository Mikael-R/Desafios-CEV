print('='*20, 'DESAFIO 19', '='*20)
print('')
from random import choice
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
sorteado = choice(alunos)
print('O(a) aluno(a) sorteado(a) foi {}.'.format(sorteado))
