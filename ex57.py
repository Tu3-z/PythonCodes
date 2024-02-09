s = str(input('Digite seu sexo [F/M]: ')).upper()
while s not in 'MmFf':
    s = str(input('Sexo inválido, digite novamente [F/M]:')).upper
print('Fim')