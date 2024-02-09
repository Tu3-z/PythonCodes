from random import randint
from time import sleep
l = []
lc = []
c = 0
n = int(input('Digite o número de jogos que você deseja: '))
while c < n:
    cont = 0
    while True:
        num = (randint(0, 60))
        cont += 1
        if num not in lc:
            lc.append(num)            
        if cont >= 6:
            break
    l.append(lc[:])
    lc.clear()
    c += 1
for j in l:
    print(j)
    sleep(1)
       
    