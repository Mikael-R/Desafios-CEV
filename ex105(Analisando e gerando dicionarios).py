print('='*15, 'DESAFIO 105', '='*15 + '\n')

def nota(*notas, sit=False):
    dicionario = {}
    dicionario["total"] = len(notas)
    dicionario["maior"] = max(notas)
    dicionario["menor"] = min(notas)
    dicionario["media"] = sum(notas) / len(notas)
    if sit:
        if dicionario["media"] > 7:
            situacao = 'boa'
        elif dicionario["media"] > 5 and dicionario["media"] < 7:
            situacao = 'recuperação'
        else:
            situacao = 'reprovado'
        dicionario["situação"] = situacao
    return dicionario


resp = nota(5, 6, 9 , 4, True)
print(resp)
