l = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        l[0].append(n)
    else:
        l[1].append(n)
print(f'Lista de números pares: {sorted(l[0])}\nLista de números ímpares: {sorted(l[1])}')
        
