p = 'RedBull', 7, 'Copo', 45, 'Notebook', 2400, 'Calça', 230, 'Tênis', 2000, 'Moletom', 270, 'Camisa', 80, 'Brinco', 20
cont = 0
print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-' * 50)
for c in p:
    cont += 1
    if cont % 2 == 0:
        print(f'R$ {c:.2f}')
    else:
        print(f'{c:.<30}', end='')
print('=' * 50)

        