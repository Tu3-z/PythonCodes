from random import randint
o = ''
s = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    o = input('Escolha ímpar ou par [P/I]: ').strip().upper()[0]
    np = randint(0, 11)
    s = n + np
    if s % 2 == 0 and o == 'P':
        print(f'O computador escolheu {np}, a soma vale {s}, é PAR\nVocê venceu!')
        c += 1
    elif s % 2 != 0 and o == 'I':
        print(f'O computador escolheu {np}, a soma vale {s}, é ÍMPAR\nVocê venceu!')
        c += 1
    else:
        if o == 'P':
            print(f'O computador escolheu {np}, a soma vale {s}, é ÍMPAR\nVocê perdeu!')
            break
        if o == 'I':
            print(f'O computador escolheu {np}, a soma vale {s}, é PAR\nVocê perdeu!')
            break
print(f'Você venceu {c} vezes')

        
        
    
    