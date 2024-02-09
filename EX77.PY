p = 'GARRAFA', 'TECLADO', 'TELEVISAO', 'BANANA', 'CUBO MAGICO', 'MESA', 'MONITOR', 'DIPLOMA', 'COOLER'
for c in p:
    print(f'A palavra {c} tem as seguintes vogais: ', end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end=' ')
    if True:
        print('')
        
    
    