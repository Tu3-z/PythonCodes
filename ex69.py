d = 'CADASTRO'
c1 = c2 =  c3 = 0
s = 'M' 
o = 'S'
while True:
    print(f'{d:-^15}')
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo [M/F]: ').strip().upper()[0]
    while s not in 'MF': 
        s = input('Digite o sexo[M/F]: ').strip().upper()[0]
    if i > 18:
        c1 += 1
    if s == 'M':
        c2 += 1
    if i < 20 and s == 'F':
        c3 += 1
    o = input('Deseja continuar [S/N]: ').strip().upper()[0]
    while o not in 'SN':
        o = input('Deseja continuar [S/N]: ').strip().upper()[0]
    if o == 'N':
        break
print(f'Total de pessoas maiores de 18 anos: {c1}\nTotal de homens cadastrados: {c2}\nTotal de mulheres com menos de 20 anos: {c3}')
    
