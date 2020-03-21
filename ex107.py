def metade(num):
    num = float(num)
    calculo = f'{num / 2:.2f}'
    return calculo


def dobro(num):
    num = float(num)
    calculo = f'{num * 2:.2f}'
    return calculo


def aumentar(num, porcentagem):
    num = float(num)
    porcentagem = float(porcentagem)
    calculo = f'{num + (num / porcentagem):.2f}'
    return calculo


def diminuir(num, porcentagem):
    num = float(num)
    porcentagem = float(porcentagem)
    calculo = f'{num - (num / porcentagem):.2f}'
    return calculo
