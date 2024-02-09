n = []
s = []
menor = 0
for c in range(0,5):
    n.append(int(input(f'Digite o {c} número: ')))
for p, n2 in enumerate(n):
    if p == 0:
        maior = n[0]
        menor = n[0]
        s.append(n[0])
    elif n2 > maior:
        maior = n[p]
        s.append(n[p])
    elif n2 < menor:
        menor = n[p]
        s.insert(0, n[p])
    else:
        s.insert(1, n[p])

print(s)