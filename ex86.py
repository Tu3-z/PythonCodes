l = [[ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ], [ ]]
co = 0
lin = 0
cont = 0
for c in range(0, 9):
    n = int(input(f'Digite um valor para: [{co}, {lin}]: '))
    if lin == 2:
        lin -= lin
        co += 1
    else:
        lin += 1
    l[c].append(n)
for m in l:
    cont += 1
    if cont == 4:
        cont -= cont
        cont += 1
        print(f'\n{ m }', end= ' ')
    else:
        print(f'{ m }', end=' ')
    
