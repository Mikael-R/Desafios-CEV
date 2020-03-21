print('='*20, 'DESAFIO 23', '='*20)
print('')
número = input('Digite um número de 0 a 9999: ').strip()
num = '000' + número                 # Adiciona 000 ao número 
print('Unidade: {}'.format(num[-1])) # Pega o último número
print('Dezena:  {}'.format(num[-2])) # Pega o penúltimo
print('Centena: {}'.format(num[-3])) # Pega o antepenúltimo
print('Milhar:  {}'.format(num[-4])) # Assim por diante
