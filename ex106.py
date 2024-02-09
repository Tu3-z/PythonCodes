from time import sleep

def ajuda():
    x = ''
    while x != 'fim':
        x = str(input('Biblioteca ou função > ')).lower().strip()
        print(f'\033[0;44mProcurando info sobre o comando {x}\033[m')
        sleep(1)
        print(f'\033[0;40m{help(x)}\033[m')
        print('\033[0;42mSistema de ajuda pyHelp\033[m')
        x = str(input('Biblioteca ou função > ')).lower().strip()
    print('\033[0;44mVolte sempre :)\033[m')
    quit()
    
    
ajuda()