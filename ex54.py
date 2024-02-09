contador = 0
for c in range(1, 8):
    i = int(input('Digite o ano de seu nascimento: '))
    if 2023 - i >= 21:
        contador += 1
print('De acordo com a lista digitada, {} pessoas já alcançaram a maioridade e {} ainda não'.format(contador, 7 - contador))