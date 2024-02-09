n = c = 0
while True:
    n = int(input('Digite um número: '))
    if n < 0 :
        break
    for c in range(1, 10):
        c += 1
        r = n * c
        print(f'{n} x {c} = {r}')
    print('-'*15)
print('Programa interrompido')
              