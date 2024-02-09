p = []
cont = 0
d = []
o = 'S'
while o == 'S':
    p.append(str(input('Digite o nome: ')))
    cont += 1
    p.append(int(input('Digite o peso: ')))
    d.append(p[:])
    p.clear()
    o = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while o not in 'SN':
        o = str(input('Tente novamente. Deseja continuar? [S/N]: ')).strip().upper()
print(f'Foram cadastradas {cont} pessoas')
maior = 0
menor = 0
for r, c in enumerate(d):
    if r == 0:
        maior = c[1]
        menor = c[1]
    else:
        if c[1] > maior:
            maior = c[1]
        if c[1] < menor:
            menor = c[1]
            
print(f'O maior peso é {maior} Kg, peso de ', end = ' ')
for mai in d:
    if maior in mai:
        print(f'{mai[0]}', end = '..')

print(f'\nO menor peso é {menor} Kg, peso de ', end = ' ')
for men in d:
    if menor in men:
        print(f'{men[0]}', end = '..')
