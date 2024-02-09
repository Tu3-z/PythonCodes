o = 'S'
n = []
c = 0
while o == 'S':
    n.append(int(input('Digite um valor: ')))
    o = input('Deseja continuar? [S/N]: ').strip().upper()
    while o not in 'SN':
        o = input('Tente novamente. Deseja continuar? [S/N]: ').strip().upper()
for num in n:
    c += 1
    if c > 0:
        if num in n[:c]:
            n.remove(n[c])
            c -= 1
print(sorted(n))
            
