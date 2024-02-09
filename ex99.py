from random import randint
from time import sleep

def maior(* n):
    for p, v in enumerate(n):
        if p == 0:
            maior = v
        elif v >= maior:
            maior = v
    if len(n) == 0:
        print('foram informados 0 valores\nO maior é 0')
    else:
        print(f'números escolhidos: {n}, {len(n)} no total.')
        print(f'O maior é {maior}')
    sleep(1)
maior(5, 2, 5, 9, 10, 8) 
maior(0, 4, 10)
maior(0, 1)
maior(2)   
maior()