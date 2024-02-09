s = 0
for c in range(0 , 500):
    if (c % 3) == 0 and (c % 2) != 0:
        s = s + c
print('A soma total deu {}'.format(s))
