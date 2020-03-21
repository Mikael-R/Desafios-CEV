print('='*15, 'DESAFIO 56', '='*15, '\n')
cont1 = 0
cont2 = 0
maior = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').strip().upper()
    cont1 = cont1 + idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            nomeM = nome
    elif sexo == 'F':
        if idade < 20:
            cont2 = cont2 + 1
media = cont1 / 4
print('\nA media de idade do grupo é de {:.1f} anos.'.format(media))
print('O homem mais velho se chama {}.'.format(nomeM))
print('{} mulher(es) tem menos de 20 anos.'.format(cont2))
