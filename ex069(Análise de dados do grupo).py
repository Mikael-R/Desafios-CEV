print('='*15, 'DESAFIO 69', '='*15)
cont_18 = cont_m = cont_f = 0
while True:
    idade = int(input('\nIdade da pessoa: '))
    sexo = str(input('Gênero [Masculino/Feminino]: ')).strip().lower()
    while sexo != 'masculino' and sexo != 'feminino':
        sexo = str(input('Gênero [Masculino/Feminino]: ')).strip().lower()
    if idade > 18:
        cont_18 += 1
    if sexo == 'masculino':
        cont_m += 1
    if sexo == 'feminino' and idade < 20:
        cont_f += 1
    continuar = str(input('\nQuer continuar [Sim/Não]: ')).strip().lower()
    while continuar != 'sim' and continuar != 'não':
        continuar = str(input('Quer continuar [Sim/Não]: ')).strip().lower()
    if continuar == 'não':
        break
print(f'\nPessoas com mais de 18 anos: {cont_18}')
print(f'Homens cadastrados: {cont_m}')
print(f'Mulheres com mais de 20 anos: {cont_f}')
