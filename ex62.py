n = int(input('Digite um número: '))
t1 = 0
t2 = 1
t3 = 1
print('{} - {} '.format(t1 , t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' - {} - '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('fim')