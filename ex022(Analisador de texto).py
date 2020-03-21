print('='*20, 'DESAFIO 22', '='*20)
print('')
nome = input('Nome completo: ').strip().title() #.strip:Retira o espaço antes depois do nome / .title:Deixa a primeira letra após o espaço maiúscula
print('Analisando o nome...')
nome1 = nome.split()
print('O nome em maiúsculo é {}.'.format(nome.upper()))
print('O nome em minusculas é {}.'.format(nome.lower()))
print('O nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nome1[0], nome.find(' ')))
