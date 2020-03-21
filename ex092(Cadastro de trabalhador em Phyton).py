print('='*15, 'DESAFIO 92', '='*15 + '\n')

trabalhador = {'nome': input('Nome: ').strip()}

trabalhador["nascimento"] = input('Ano de nascimento: ').strip()
while not trabalhador["nascimento"].isnumeric():
    print('Digite apenas números.')
    trabalhador["nascimento"] = input('Ano de nascimento: ').strip()

trabalhador["carteira"] = input('Número da carteira de trabalho [0 não tem]: ').strip()
while not trabalhador["carteira"].isnumeric():
    print('Digite apenas números.')
    trabalhador["carteira"] = input('Número da carteira de trabalho [0 não tem]: ').strip()

if trabalhador["carteira"] != '0':
    trabalhador["contratacao"] = input('Ano de contratação: ').strip()
    while not trabalhador["contratacao"].isnumeric():
        print('Digite apenas números')
        trabalhador["contratacao"] = input('Ano de contratação: ').strip()

    trabalhador["salario"] = input('Salário: R$').strip()
    while not trabalhador["salario"].isnumeric():
        print('Digite apenas números')
        trabalhador["salario"] = input('Salário: R$').strip()

    trabalhador["aposentadoria"] = int(trabalhador["contratacao"]) - int(trabalhador["nascimento"]) + 35

print(f'\nNome: {trabalhador["nome"]}')
print(f'Nascimento : {trabalhador["nascimento"]}')
if trabalhador["carteira"] != '0':
    print(f'Número da CNH: {trabalhador["carteira"]}')
    print(f'Ano de contratação: {trabalhador["contratacao"]}')
    print(f'Salário: R${float(trabalhador["salario"]):.2f}')
    print(f'Aposentadoria: {trabalhador["aposentadoria"]} anos.')
