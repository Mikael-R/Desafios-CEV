print('='*15, 'DESAFIO 108', '='*15 + '\n')

from ex108 import metade, dobro, aumentar, diminuir, moeda

preco = input('Digite o preço: R$').strip()
print(f'A metade de R${preco} é {moeda(metade(preco))}')
print(f'O dobro de R${preco} é {moeda(dobro(preco))}')
print(f'Aumentando 10% de R${preco} temos {moeda(aumentar(preco, 10))}')
print(f'Diminuindo 10% de R${preco} temos {moeda(diminuir(preco, 10))}')
