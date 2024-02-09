from random import randint
from time import sleep

l = []
def sorteia(x):
    for c in range(0, 5):
        x.append(randint(0, 10))
    print('Números sorteados: ')
    for v in x:
        print(v, end=' ')
        sleep(0.3)
def somapar(x):
    s = 0
    for v in x:
        if v % 2 == 0:
            s += v
    print(f'\nSoma dos números pares: {s}')
sorteia(l)
somapar(l)