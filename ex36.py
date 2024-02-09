valc = float(input('Digite o valor do imóvel: '))
sal = float(input('Digite o seu salário: '))
anos = float(input('Digite a quantidade de anos suficientes para pagar: '))
pmes = float(valc / (anos * 12))
p = float((30 * sal) / 100) 
if pmes > p:
    print('Você não pode esse empréstimo pois o valor por mês ultrapassou 30% do sálario digitado')
elif pmes < p:
    print('De acordo com essas informaçôes: \nValor do imóvel: R${:.2f} \nSalário ganho: R${:.2f} \nTotal à pagar por mês: R${:.2f} \nAnos para pagar: {}'.format(valc, sal, pmes, anos))    