c = 0
maior = 0
menor = 0
o = 'S'
soma = 0
while o == 'S':
    n = int(input('Digite um número: '))
    c += 1
    soma += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor: 
            menor = n
    o = input('Deseja continuar? [S/N]: ').upper()
    

print('Fim do programa\nA média dos números digitados foi {:.2f}\nMaior: {}\nMenor: {}'.format(soma / c, maior, menor ))