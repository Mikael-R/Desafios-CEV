print('='*15, 'DESAFIO 77', '='*15 + '\n')
valores = []
posicoesMaior = []
posicoesMenor = []
maior = menor = 0

for i in range(0, 5):
    numero = int(input(f'Digite um valor para a posição {i}: '))
    valores.append(numero)

    if i == 0:
        maior = menor = valores[i]
    elif valores[i] > maior:
        maior = valores[i]
    elif valores[i] < menor:
        menor = valores[i]

for i in range(0, 5):
    if valores[i] == maior:
        posicoesMaior.append(i)
    if valores[i] == menor:
        posicoesMenor.append(i)


print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao in posicoesMaior:
    print(posicao, end='... ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for posicao in posicoesMenor:
    print(posicao, end='... ')
