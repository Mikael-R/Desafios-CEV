print('='*15, 'DESAFIO 63', '='*15 + '\n')
print('-_-'*8 + '\nSequência de Fibonacci\n' + '-_-'*8)
termos = int(input('\nQuantos termos deseja: '))

termos_cont = 1
anterior = 0
proxima = 1
soma = 1

while termos_cont <= termos:
     print(anterior, end=' - ')
     termos_cont += 1
     soma = proxima + anterior
     anterior = proxima
     proxima = soma
print('FIM')
