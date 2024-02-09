total = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1) :
    if n % c == 0:
        total += 1
if total == 2 :
    print('O número {} é primo'.format(n))
else :
    print('O número {} não é primo'.format(n))
        