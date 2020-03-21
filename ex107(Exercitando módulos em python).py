print('='*15, 'DESAFIO 107', '='*15, '\n')
from ex107 import metade, dobro, aumentar, diminuir

preco = float(input('Digite o preço: R$').strip())
print(f'A metade de R${preco:.2f} é R${metade(preco)}')
print(f'O dobro de R${preco:.2f} é R${dobro(preco)}')
print(f'Aumentando 10% de R${preco:.2f} temos R${aumentar(preco, 10)}')
print(f'Diminuindo 10% de R${preco:.2f} temos R${diminuir(preco, 10)}')
