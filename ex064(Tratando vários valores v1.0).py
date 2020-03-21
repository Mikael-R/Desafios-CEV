print('='*15, 'DESAFIO 64', '='*15, '\n')
num = int(input('Digite um número [999 para parar]: '))
cont = soma = 0
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [999 para parar]: '))
if cont == 0:
    print('Não foi digitado nenhum número!')
else:
    print('Foram digitados {} números e a soma entre eles é {}.'.format(cont, soma))
