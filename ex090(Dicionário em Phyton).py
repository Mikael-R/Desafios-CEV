print('='*15, 'DESAFIO 90', '='*15 + '\n')
aluno = {'Nome': str(input('Nome: ')), 'Media': float(input('Média: '))}
if aluno['Media'] < 7:
    aluno['Situação'] = 'reprovado'
else:
    aluno['Situação'] = 'aprovado'
print('-'*18)
for k, v in aluno.items():
    print(f'{k} é {v}.')
