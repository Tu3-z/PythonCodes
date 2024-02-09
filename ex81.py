o = 'S'
n = []
r = []
while o == 'S':
    n.append(int(input('Digite um número: ')))
    n.sort(reverse=True)
    o = input('Deseja continuar? [S/N]: ').strip().upper()
    while o not in 'SN':
        o = input('Tente novamente. Deseja continuar? [S/N]: ').strip().upper()
print(f'Quantidade de números digitados: {len(n)}\nValores em ordem descrecente: {n}')
if 5 in n:
    print('A lista contém o número 5')
else:
    print('A lista não contém o número 5')
