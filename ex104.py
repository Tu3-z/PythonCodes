def leiaint(t):
    ok = False
    v = 0       
    while True:
        n = str(input(f'{t}'))        
        if n.isnumeric():
            ok = True
            v = int(n)
        else:
            print('Erro! Deve ser um número inteiro.')
        if ok:
            return v 


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
