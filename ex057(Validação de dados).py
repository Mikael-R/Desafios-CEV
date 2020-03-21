print('='*15, 'DESAFIO 57', '='*15, '\n')
genero = str(input('Informe um gênero [M/F]: ')).upper().strip()
while genero[0] not in 'MF':
    genero = str(input('Dados inválidos. Informe um gênero válido: ')).upper().strip()
