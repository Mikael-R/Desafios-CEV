print('='*15, 'DESAFIO 53', '='*15, '\n')
frase = input('Digite uma frase: ').lower().strip().replace(' ', '')
invertida = frase[::-1]
if frase == invertida:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
