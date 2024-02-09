l = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for li in range(0, 3):
        l[c][li] = int(input(f'Digite um número na posição [{c}, {li}]: '))

for c in range(0, 3):
    for li in range(0,3):
        print(f'{l[c][li]:^5}', end='')
    print()
    
s = 0
s2 = 0
maior = 0
for c in range(0, 3):
    for li in range(0,3):
        if l[c][li] % 2 == 0:
            s += l[c][li]
        if li == 2:
            s2 += l[c][li]
        if c == 1:
            if li == 0:
                maior = l[c][li]
            else:
                if l[c][li] > maior:
                    maior = l[c][li]
print(f'Soma dos números pares: {s}')
print(f'Soma dos números da terceira coluna: {s2}')
print(f'Maior valor da segunda linha: {maior}')
