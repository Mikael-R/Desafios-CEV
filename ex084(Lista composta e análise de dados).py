print('='*15, 'DESAFIO 81', '='*15)
nomes = []
nomeMaior = []
nomeMenor = []
maior = menor = 0
while True:
    nome = str(input('\nNome: ')).title()
    nomes.append(nome)
    peso = float(input('Peso: '))
    if maior == 0 and menor == 0:
        maior = peso
        nomeMaior.append(nome)
        menor = peso
        nomeMenor.append(nome)
    else:
        if peso == maior:
            nomeMaior.append(nome)
        if peso > maior:
            maior = peso
            nomeMaior.clear()
            nomeMaior.append(nome)
        if peso == menor:
            nomeMenor.append(nome)
        if peso < menor:
            menor = peso
            nomeMenor.clear()
            nomeMenor.append(nome)
    continuar = str(input('Deseja continuar [sim/não]: ')).strip().lower()
    while continuar != 'sim' and continuar != 'não':
        print('Digite corretamente.')
        continuar = str(input('\nDeseja continuar [sim/não]: ')).strip().lower()
    if continuar == 'não':
        break
print(f'\nAo todo você cadastrou {len(nomes)} pessoas.')
print(f'Maior peso: {maior:.1f}Kg de {nomeMaior}')
print(f'Menor peso: {menor:.1f}Kg de {nomeMenor}')
