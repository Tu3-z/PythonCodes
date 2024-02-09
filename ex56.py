maior = 0
contador = 0
soma = 0
nomevelho = ''
media = 0
for c in range(1, 5):
    print('------------- {} pessoa --------------'.format(c))
    n = input('Digite o nome: ')
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo [F/M]: ').upper()
    if c == 1 and s == 'M':
        maior = i
        nomevelho = n
    else:
        if i > maior and s == 'M':
            maior = i
            nomevelho = n
    if s == 'F' and i < 20:
        contador += 1
soma += i
media += soma / 4
print('A média de idade do grupo é {}\nO nome do homem mais velho é {} e tem {} anos\nContém {} mulheres menores de 20 anos'.format(media, nomevelho, maior, contador))
    


        
    
    