l = []
l2 = []
l3 = []
o = 'S'
c = 0
c2 = 0
while o == 'S':
    nome = input('Digite o nome do aluno: ')
    l2.append(nome)
    nota1 = int(input('Digite a nota 1: '))
    nota2 = int(input('Digite a nota 2: '))
    l3.append(nota1)
    l3.append(nota2)
    l2.append(l3[:])
    l.append(l2[:])
    l2.clear()
    l3.clear()
    c += 1
    o = input('Deseja continuar? [S/N]: ')
    while o not in 'SN':
        o = input('Tente novamente. Deseja continuar? [S/N]: ')
        
m = []
while True:
    for me in l:
        m.append(((me[1][0] + (me[1][1])) / 2))
        c2 += 1
    if c2 == c:
        break

print('-'*25)
for po, d in enumerate(l):
    print(f'{po}   {d[0]}   {m[po]}')
print('-'*25)

while True:
    op = int(input('Digite o número do aluno para ver as notas do tal: (999 interrompe): '))
    if op == 999:
        print('Programa finaizado')
        break
    print('-'*25)
    print(f'As notas do(a) aluno(a) {l[op][0]} são: {l[op][1]}')
    print('-'*25)
    if op == 999:
        print('Programa finaizado')
        break