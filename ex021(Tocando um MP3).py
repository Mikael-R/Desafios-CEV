print('='*15, 'DESAFIO 21', '='*15 + '\n')
from pygame import mixer
import os.path

mixer.init()
opcao = volume = 0.3

musica = str(input('\nQual música deseja tocar: '))
while not os.path.exists(musica):
    print(f'>>> O arquivo "{musica}" não foi encontrado.')
    musica = str(input('\nQual música deseja tocar: '))
mixer.music.load(musica)
mixer.music.set_volume(0.3)
mixer.music.play()
print(f'>>> A música "{musica}" foi iniciada.')

print('''
======= OPÇÕES =======
[0] Sair
[1] Substituir
[2] Reiniciar
[3] Pausar / Despausar
[4] Volume 
[5] Mudar volume''')

while opcao != 0:
    opcao = int(input('\nQual sua opção: '))

    if opcao == 1:
        musica = str(input('\nQual música deseja substituir a atual ["." para voltar]: '))
        if musica == '.':
            print('''
======= OPÇÕES =======
[0] Sair
[1] Substituir
[2] Reiniciar
[3] Pausar / Despausar
[4] Volume 
[5] Mudar volume''')
        else:
            while not os.path.exists(musica):
                print(f'>>> O arquivo "{musica}" não foi encontrado.')
                musica = str(input('\nQual música deseja substituir a atual: '))
            mixer.music.load(musica)
            mixer.music.set_volume(0.3)
            mixer.music.play()
            print(f'>>> A música "{musica}" foi iniciada.')

    if opcao == 2:
        print('>>> Música reiniciada.')
        mixer.music.rewind()

    if opcao == 3:
        print('>>> Música pausada.')
        mixer.music.pause()
        despausar = int(input('Pressione 3 novamente para despausar: '))
        while despausar != 3:
            despausar = int(input('Pressione 3 novamente para despausar: '))
        if despausar == 3:
            print('>>> Música despausada.')
            mixer.music.unpause()

    if opcao == 4:
        print(f'>>> O volume da música é {mixer.music.get_volume():.1f}!')

    if opcao == 5:
        volume = float(input('Digite o volume da música [0.0 até 1.0]: '))
        while volume > 1.0 or volume < 0:
            print('>>> O volume suportado é entre 0.0 e 1.0!')
            volume = float(input('Digite o volume da música [0.0 até 1.0]: '))
        mixer.music.set_volume(volume)

print('\nPrograma finalizado!')
