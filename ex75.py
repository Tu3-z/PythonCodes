n = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))
a = n.count(9)
if 3 in n:
    print(f'O número 3 está na {n.index(3) + 1}º posição')
else:
    print('O número 3 não foi digitado')
print(f'Vezes que o 9 foi digitado: {a}')
print(f'Números pares: ', end='')
for c in n:
    if c % 2 == 0:
        print(c , end=' ')
    
