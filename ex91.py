from random import randint
from time import sleep
from operator import itemgetter
n = {}
n['jogador 1'] = randint(1, 6)
n['jogador 2'] = randint(1, 6)
n['jogador 3'] = randint(1, 6)
n['jogador 4'] = randint(1, 6)
for k, v in n.items():
    print(f'O {k} tirou {v}')
    sleep(1)
r = []
c = 0
r = sorted(n.items(), key=itemgetter(1), reverse=True)
for p, nu in r:
    c += 1
    print(f'{c}º lugar: {p}: {nu}')
    