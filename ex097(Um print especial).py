print('='*15, 'DESAFIO 97', '='*15 + '\n')

def escreva(msg):
    print('-'* (len(msg) + 4))
    print(f'  {msg}  ')
    print('-'* (len(msg) + 4))
    
    
def continuar():
    continuar = input('Deseja continuar [sim/não]: ').strip().lower()
    while continuar != 'sim' and continuar != 'não':
        print('Resposta inválida.')
        continuar = input('Deseja continuar [sim/não]: ').strip().lower()
    if continuar == 'não':
        exit()
    print('')

        
while True:
    mensagem = input('Digite algo: ').strip()
    escreva(mensagem)
    continuar()
