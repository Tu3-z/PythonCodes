n = []
p = []
i = []
o = 'S'
while o == 'S':
    n.append(int(input('Digite um número: ')))
    o = input('Deseja continuar? [S/N]: ').strip().upper()
    while o not in 'SN':
        o = input('Tente novamente. Deseja continuar? [S/N]: ').strip().upper()
for c, n2 in enumerate(n):
    if n2 % 2 == 0:
        p.append(n2)
    else:
        i.append(n2)
print(f'Lista digitada: {n}\nLista com apenas números pares: {p}\nLista com apenas números ímpares: {i}')