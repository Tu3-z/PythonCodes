def notas(* n, sit=False):
    d = {}
    d['Total'] = len(n)
    s = 0
    for p, c in enumerate(n):
        s += c
        if p == 0:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    d['Maior'] = maior
    d['Menor'] = menor
    d['Média'] = (s / len(n))
    if sit:
        if d['Média'] >= 7:
            d['situação'] = 'BOA'
        elif d['Média'] < 7 and d['Média'] >= 6:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'RUIM'
    return d


print(notas(10, 5, 4, sit=True))