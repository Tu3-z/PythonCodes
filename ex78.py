n = []
for c in range(0, 5):
    n.append(int(input(f'Digite o {c} número: ')))
print(f'Você digitou os valores {n}')
print(f'Maior número: {max(n)}\nMenor número: {min(n)}')
print('Posição do maior número: ', end='')
for pma, num in enumerate(n):
    if num == max(n):
        print(f'{pma}', end='..')
print('\nPosição do menor número: ',end='')
for pme, num in enumerate(n):
    if num == min(n):
        print(f'{pme}', end='..')
        
        
        
