l = []
e = input('Digite sua expressão: ')
for s in e:
    if s == '(':
        l.append('(')
    elif s == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append('-')
if len(l) == 0:
    print('Expressão correta')
else:
    print('Expressão incorreta')