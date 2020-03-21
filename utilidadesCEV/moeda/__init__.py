def metade(num, formatado=False, moeda='R$'):
    num = float(num)
    calculo = f'{num / 2:.2f}'
    if formatado==True:
        num = str(calculo)
        return f'{moeda}{calculo}'.replace('.', ',')
    else:
        return calculo


def dobro(num, formatado=False, moeda='R$'):
    num = float(num)
    calculo = f'{num * 2:.2f}'
    if formatado==True:
        num = str(calculo)
        return f'{moeda}{calculo}'.replace('.', ',')
    else:
        return calculo


def aumentar(num, porcentagem, formatado=False, moeda='R$'):
    num = float(num)
    porcentagem = float(porcentagem)
    calculo = f'{num + (num / porcentagem):.2f}'
    if formatado==True:
        num = str(calculo)
        return f'{moeda}{calculo}'.replace('.', ',')
    else:
        return calculo


def diminuir(num, porcentagem, formatado=False, moeda='R$'):
    num = float(num)
    porcentagem = float(porcentagem)
    calculo = f'{num - (num / porcentagem):.2f}'
    if formatado==True:
        num = str(calculo)
        return f'{moeda}{calculo}'.replace('.', ',')
    else:
        return calculo


def resumo(num, num_aumento=0, num_reducao=0):
    num = float(num)
    num_aumento = float(num_aumento)
    num_reducao = float(num_reducao)

    metade = num / 2
    dobro = num * 2
    aumento = ((num_aumento * num)  / 100) + num
    reducao = ((num_reducao * num)  / 100) + num

    barra_padrao = '-------------------------------'
    barra = '-' * (len(str(dobro)))
    if len(barra_padrao) > len(barra):
        barra = barra_padrao

    print(f'''
{barra}
        RESUMO DO VALOR
{barra}
Preço analisado:       R${num:.2f}
Metade do preço:       R${metade:.2f}
Dobro do preço:        R${dobro:.2f}''')

    if num_aumento > 0:
        print(f'{num_aumento}% de aumento:       R${aumento:.2f}')
    if num_reducao > 0:
        print(f'{num_reducao}% de redução:       R${reducao:.2f}')

    print(barra + '\n')
