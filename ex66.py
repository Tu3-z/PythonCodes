n = c = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} números\nA soma de todos eles vale {s}')