p = str(input('Digite uma frase ou palavra: ')).upper().strip()
pt = p.split()
pn = ''.join(pt)
inv = ''
for l in range(len(pn) - 1, -1, -1):
       inv += pn[l]
if pn == inv :
    print('A palavra digitada é um palíndromo')
else :
    print('Essa palavra não é um palíndromo')