print('='*15, 'DESAFIO 109', '='*15 + '\n')

from ex109 import metade, dobro, aumentar, diminuir

preco = input('Digite o preço: R$').strip()
print(f'A metade de R${preco} é {metade(preco, True)}')
print(f'O dobro de R${preco} é {dobro(preco, True)}')
print(f'Aumentando 10% de R${preco} temos {aumentar(preco, 10, True)}')
print(f'Diminuindo 10% de R${preco} temos {diminuir(preco, 10, True)}')
