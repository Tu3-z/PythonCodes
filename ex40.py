n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = float((n1 + n2) / 2)
if m < 5 :
    print('O aluno(a) foi REPROVADO')
elif m >= 5 and m <= 6.9 :
    print('O aluno(a) está de RECUPERAÇÃO')
elif m >= 7 and m <= 10 :
    print('O aluno(a) foi APROVADO')
else :
    print('Média inválida')