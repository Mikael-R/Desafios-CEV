print('='*20, 'DESAFIO 11', '='*20)
print('')
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, lar*alt))    #Para subir um número aperte cntr+alt
print('Para pintar essa parede, você precisará de {}L de tinta.'.format((alt*lar)/2))
