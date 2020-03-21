def resumo(num, num_aumento, num_reducao):
    num = float(num)
    metade = num / 2
    dobro = num * 2
    aumento = ((num_aumento * num)  / 100) + num
    reducao = ((num_reducao * num)  / 100) + num

    barra_padrao = '-------------------------------'
    barra = '-' * (len(str(dobro)) * 3)
    if len(barra_padrao) > len(barra):
        barra = barra_padrao
    print(f'''
{barra}
        RESUMO DO VALOR
{barra}
Preço analisado:       R${num:.2f}
Metade do preço:       R${metade:.2f}
Dobro do preço:        R${dobro:.2f}
{num_aumento}% de aumento:        R${aumento:.2f}
{num_reducao}% de redução:        R${reducao:.2f}
{barra}
''')