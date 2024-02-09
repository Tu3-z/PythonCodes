p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = float(p / (a * a))
if imc < 18.5 :
    print('IMC: {:.1f}\nAbaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25 :
    print('IMC : {:.1f}\nPeso ideal'.format(imc))
elif imc >= 25 and imc <= 30 :
    print('IMC : {:.1f}\nSobrepeso'.format(imc))
elif imc >= 30 and imc <= 40 :
    print('IMC : {:.1f}\nObesidade'.format(imc))
else :
     print('IMC : {:.1f}\nObesidade mórbida'.format(imc))
