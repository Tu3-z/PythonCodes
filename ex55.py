maior = 0
menor = 0
for c in range(1, 6):
    p = int(input('Digite um peso: '))
    if c == 1:
        maior = p 
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O menor peso é {} e o maior é {}'.format(menor, maior))
    
