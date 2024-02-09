s = menor = c = cp = 0
nmenor = ''
while True:
    n = (input('Digite o nome do produto: '))
    p = float(input('Digite o preço do produto: '))
    c += 1
    s += p
    if c == 1:
        menor = p
        nmenor = n
    elif p < menor:
        menor = p
        nmenor = n
    if p > 1000:
        cp += 1
    o = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while o not in 'SN':
        o = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if o == 'N':
        break
print(f'Total gasto: R${s}\nProdutos que custam mais de R$1000: {cp}\nNome do produto mais barato: {nmenor}')


        
        
        