n = 0
soma = 0
c = 0
while n != 999:
    n = int(input('Digite um número: ').format(c))
    soma += n
    c += 1
print('A soma de todos os números desconiderando o 999 foi {}\nE foi digitado {} números tirando o 999'.format(soma - 999, c - 1))
    