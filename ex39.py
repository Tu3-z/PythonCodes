i = int(input('Digite a sua idade: '))
if i == 18 :
    print('Você deve se alistar')
elif i < 18 :
    print('Você ainda não precisa se alistar, somente daqui {} ano(s)'.format(18 - i))
elif i > 18 :
    print('Já passou {} ano(s) da idade adequada para alistamento'.format(i - 18))