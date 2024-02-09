c50 = c20 = c10 = c1 = 0
s = 0
n = int(input('Digite quanto você quer sacar: '))
while True:
    c50 = int(n / 50)
    s = 50 * c50
    while (s // 1 % 10) < (n // 1 % 10):
        s += 1
        c1 += 1
    if (n // 10 % 10) > 2 and (20 + s) <= n:
        s += 20
        c20 += 1
    if(n // 10 % 10) > 1 and (10 + s) <= n:
        s += 10
        c10 += 1
    if s == n:
        break    
print(f'Notas de 50: {c50}\nNotas de 20: {c20}\nNotas de 10: {c10}\nMoedas de 1: {c1}')  