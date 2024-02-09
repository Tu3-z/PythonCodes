n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
o = 0
while o != 5:
    o = int(input('''Digite a opção desejada:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos números
[5] Finalizar programa
Sua opção: ''')) 

    if o == 1:
        print('A soma dos dois números é igual a {}'.format(n1 + n2))
        print('------------------------------')
    elif o == 2:
        print('A multiplicação dos dois números é igual a {}'.format(n1 * n2))
        print('------------------------------')
    elif o == 3:
        if n1 > n2:
            print('O maior número é o {}'.format(n1))
            print('------------------------------')
        else:
            if n1 > n2:
                print('O maior número é o {}'.format(n2))
            else:
                print('Os números são iguais')
            print('------------------------------')
    elif o == 4:
        print('digite os números novamente')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    else:
        print('Opção inválida, tente novamente')
print('Programa encerrado')
        