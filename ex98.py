from time import sleep
def contagem():
    for co in range(0, 11):
        print(co, end=' ')
        sleep(0.5)
    print('FIM')
    for co in range(10, -2, -2):
        print(co, end=' ')
        sleep(0.5)
    print('FIM')
    print('Sua vez!')
    x = int(input('Inicio: '))
    y = int(input('Fim: '))
    z = int(input('Passo: '))
    if z == 0:
        z = 1
    for co in range(x, y, z):
        print(co, end=' ')
        sleep(0.5)
    print('FIM')
print(contagem())
        
        