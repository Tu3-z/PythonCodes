from random import randint
n = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
maior = 0
menor = 0
for c in n:
    if c == 1:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
print(f'Números escolhidos: {n}\nMaior: {maior}\nMenor: {menor}')