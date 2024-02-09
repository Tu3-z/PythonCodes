d1 = {}
i = []
l = []
m = []
s = 0
c = 0
o = 'S'
while o == 'S':
    c += 1
    d1['nome'] = str(input('Nome: '))
    d1['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()
    while d1['sexo'] not in 'MF':
        print('Erro! Digite M ou F')
    if d1['sexo'] == 'F':
        m.append(d1['nome'])
    d1['idade'] = int(input('Idade: '))
    i.append(d1['idade'])
    s += d1['idade']
    l.append(d1.copy())
    o = input('Deseja continuar? [S/N]: ').upper().strip()
    while o not in 'SN':
        print('Erro! Digite S ou N')
me = s / c
print(f'Foram cadastradas {c} pessoas')
print(f'A média de idade é {me}')
print('Mulheres cadastradas: ', end='')
for mu in m:
    print(mu, end=' ')
print()

print('Pessoas acima da média de idade: ')
for p in l:
    if p['idade'] > me:
        print(f'Nome = {p["nome"]}; Sexo; {p["sexo"]}; Idade {p["idade"]};')
    