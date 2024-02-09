def fatorial(x, show=False):
    f = 1
    for c in range(x , 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f

print(fatorial(5, show=False))    