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
