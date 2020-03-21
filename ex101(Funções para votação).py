print('='*15, 'DESAFIO 101', '='*15, '\n')

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now()
    idade = ano_atual.year - ano
    
    if idade > 18 and idade < 70:
        return 'obrigatório'
    if idade < 16:
        return 'não vota'
    if idade > 70:
        return 'opcional'
    if idade < 18 and idade >= 16:
        return 'opcional'

def idade(ano):
    from datetime import datetime
    ano_atual = datetime.now()
    idade = ano_atual.year - ano
    return idade

nascimento = input('Ano de nascimento: ')
while not nascimento.isnumeric():
    print('Digite apenas números.')
    nascimento = input('Ano de nascimento: ')
nascimento = int(nascimento)

print(f'Com {idade(nascimento)} anos o voto é: {voto(nascimento)}')
