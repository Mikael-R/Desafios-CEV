print('='*15, 'DESAFIO 78', '='*15 + '\n')

listanumeros = []
for valores in range(0 ,5):
    valor = int(input(f'Digite um valor para a posição {valores}: '))
    listanumeros.append(valor)

print('-'*50)
print(f'Você digitou os valores {listanumeros}')
print(f'O maior valor digitado foi {max(listanumeros)}',end='')
print(f' e está na posição',end=' ')
for indice,maior in enumerate(listanumeros):
    if maior == max(listanumeros):
        print(f'{indice}',end=' ')
print(f'\nO menor valor digitado foi {min(listanumeros)}',end=' ')
print(f'e está na posição',end=' ')
for indice2,menor in enumerate(listanumeros):
    if menor == min(listanumeros):
        print(f'{indice2}',end=' ')
