n = int(input('Digite um número: '))
print ('''Escolha um método de conversão:
(1) Binário
(2) Hexadecimal
(3) Octal''')
op = int(input('Sua opção: '))
if op == 1 :
    print('Número convertido: {}'.format(bin(n)[2:]))
elif op == 2 :
    print('Número convertido: {}'.format(hex(n)[2:]))
elif op == 3 :
    print('Número convertido: {}'.format(oct(n)[2:]))
else :
    print('Valor inválido')