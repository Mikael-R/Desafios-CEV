print('='*15, 'DESAFIO 98', '='*15)

def contador( inicio, fim, passo):
    from time import sleep
    print('-'*30)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.5)
    if inicio > fim:
        for n in range( inicio, fim + 1, -passo):
            print( f' {n} ', end = "", flush=True)
            sleep( 0.2)
        print()
    else:
        for n in range( inicio, fim + 1, passo):
            print( f' {n} ', end = "", flush=True)
            sleep(0.2)
        print()

def continuar():
    continuar = input('Deseja continuar [sim/não]: ')  .strip().lower()
    while continuar != 'sim' and continuar != 'não':
        print('Resposta inválida.')
        continuar = input('Deseja continuar [sim/não]: ')  .strip().lower()
    if continuar == 'não':
        exit()

   
contador( 1, 10, 1)
contador( -10, -1, -1)
while True:
    print('-'*30)
    print('\nPersonalize sua contagem: ')
    inicio = int( input( 'Inicio: '))
    fim =    int( input( 'Fim:    '))
    passo =  int( input( 'Passo:  '))
    contador( inicio, fim, passo)
    continuar()
