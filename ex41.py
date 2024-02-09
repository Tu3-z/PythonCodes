print('Digite o cumprimento de três retas: ')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if (r1 + r2) > r3:
    print('É possível formar um triângulo com essas retas')
    if r1 == r2 == r3 :
        print('O triângulo formado é classificado como equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r2 or r3 == r1 :
        print('O triângulo formado é classificado como isósceles')
    else :
        print('O triângulo formado é classificado como escaleno')
else: 
    print('Não é possível formar um triângulo com essas retas')
