print('='*15, 'DESAFIO 94', '='*15)

pessoas = {}
num = 0
cont = 0
idades = []
idade_total = 0
mulheres = []
idade_media_nome = []
idade_media_idade = []
idade_media_sexo = []

while True:
    # NUMERO DO CADASTRO
    num += 1

    # NOME
    pessoas[f"pessoa_nome_{num}"] = input(f'\nNome da pessoa {num}: ').strip().title()

    # IDADE
    pessoas[f"pessoa_idade_{num}"] = input(f'Idade da pessoa {num}: ').strip()
    while not pessoas[f"pessoa_idade_{num}"].isnumeric():
        print('Digite apenas números.')
        pessoas[f"pessoa_idade_{num}"] = input(f'Idade da pessoa {num}: ').strip()

    # IDADE TOTAL
    idades.append(float(pessoas[f"pessoa_idade_{num}"]))
    for valor in idades:
        idade_total += valor

    # SEXO
    pessoas[f"pessoa_sexo_{num}"] = input(f'Sexo da pessoa {num} [masculino/feminino]: ').strip().lower()
    while pessoas[f"pessoa_sexo_{num}"] != 'masculino' and pessoas[f"pessoa_sexo_{num}"] != 'feminino':
        print('Opção inválida. Tente novamente.')
        pessoas[f"pessoa_sexo_{num}"] = input(f'Sexo da pessoa {num} [masculino/feminino]: ').strip().lower()

    # MULHERES
    if pessoas[f"pessoa_sexo_{num}"] == 'feminino':
        mulheres.append(pessoas[f"pessoa_nome_{num}"])

    # SAIR
    sair = input('Deseja continuar [sim/não]: ').strip().lower()
    while sair != 'sim' and sair != 'não':
        print('Opção inválida. Tente novamente.')
        sair = input('Deseja adicionar mais uma pessoa [sim/não]: ').strip().lower()
    if sair == 'não':
        break

print('_'*41)
# PESSOAS CADASTRADAS
print(f'-> Foram cadastradas {num} pessoas.')
# IDADE MEDIA
idade_media = idade_total // num
print(f'-> A idade média do grupo é {idade_media} anos.')
# MULHERES CADASTRADAS
print(f'-> Foram cadastradas {len(mulheres)} mulheres: ', end='')
for mulher in mulheres:
    print(mulher, end='|')
# VERIFICANDO AS PESSOAS ACIMA DA IDADE MEDIA
while cont <= num:
    if int(pessoas[f"pessoa_idade_{cont}"]) > idade_media:
        idade_media_nome.append(pessoas[f"pessoa_nome_{cont}"])
        idade_media_idade.append(pessoas[f"pessoa_idade_{cont}"])
        idade_media_sexo.append(pessoas[f"pessoa_sexo_{cont}"])
        cont += 1
# PESSOAS ACIMA DA IDADE MEDIA
print(f'\n-> Foram {cont} pessoas que passaram da idade média:')
for nome in idade_media_nome:
    print(f'|Nome: {nome}', end=' ')
for idade in idade_media_idade:
    print(f'|Idade: {idade}', end=' ')
for sexo in idade_media_sexo:
    print(f'|Sexo: {sexo}')
print('_'*41)
