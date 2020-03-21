print('='*15, 'DESAFIO 89', '='*15)
from time import sleep

alunos = list()

dados = list()  # Guarda o nome e a nota média do aluno temporariamente.
notas = list()  # Guarda as duas notas de cada aluno temporariamente.

while True:
    dados.append(str(input('\nNome: ').title()))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    dados.append(notas[:])
    dados.append((notas[0] + notas[1]) / 2)
    alunos.append(dados[:])
    # Limpa as listas para novos dados de novos alunos.
    dados.clear()
    notas.clear()

    sair = str(input('Deseja sair [sim/não]: ')).strip().lower()
    while sair != 'sim' and sair != 'não':
        sair = str(input('Deseja sair [sim/não]: ')).strip().lower()
    if sair == 'sim':
        break

# Mostra uma tabela com o índice, o nome e a média dos alunos.
print(f'\n{"=-=" * 10}\n{"Número:   NOME:        Média:"}')
for i, aluno in enumerate(alunos):
    print(f'{i:^7}  {aluno[0]:^7}  {aluno[2]:>9.1f}')
print(f'{"=-=" * 10}')

while True:
    # Pergunta o número do aluno de acordo com a tabela para ver as notas dele.
    prompt = '\nGostaria de mostrar as notas de qual aluno?\n'
    prompt += f'{"(999 para interromper o programa)":^43}'
    numero = int(input(f'{prompt}\nNúmero: '))

    # Se o número 999 for digitado, interrompe o programa.
    if numero == 999:
        print(f'\n{"=-=" * 5}\n{"FINALIZANDO..."}\n{"=-=" * 5}')
        sleep(2)
        break

    # Percorre a lista de cada aluno com o seu índice.
    for i, aluno in enumerate(alunos):
        # Verifica se o número digitado é o mesmo que o índice do aluno na lista
        # se for, mostra as notas em forma de lista e o nome do aluno.
        if numero == i:
            print('=-=' * 11)
            print(f'As notas de {aluno[0]} são {aluno[1]}')
            print('=-=' * 11)
