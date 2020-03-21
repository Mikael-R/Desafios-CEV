print('='*15, 'DESAFIO 106', '='*15)

def pyHelp(comando):
    print('_'*55)
    help(comando)
    print('_'*55)

def sair():
    sair = input('Deseja sair [sim/não]: ').strip().lower()
    while sair != 'sim' and sair != 'não':
        print('Resposta inválida.')
        sair = input('Deseja sair [sim/não]: ').strip().lower()
    if sair == 'sim':
        print('Programa encerrado.')
        exit()

def titulo(msg):
    print('-'* (len(msg) + 4))
    print(f'  {msg}')
    print('-'* (len(msg) + 4))
    

while True:  
    titulo('SISTEMA DE AJUDA PYHELP') 
    ajuda = input('\nDeseja a consultar qual comando: ').strip().lower()
    pyHelp(ajuda)
    sair()
