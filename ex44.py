p = float(input('Digite o preço do produto: '))
print('1- À vista: Dinheiro ou cheque\n2- À vista: cartão\n3- Parcelado')
c = int(input('Digite a forma de pagamento: '))
if c == 1 :
    print('Desconto de 10%!\nValor final: R${}'.format(p - (10 * p) / 100))
elif c == 2 :
    print('Desconto de 5%!\nValor final: R${}'.format(p - (5 * p) / 100))
elif c == 3 :
    pr = int(input('Digite o número de parcelas desejadas: '))
    if pr == 2 :
        print('Valor final: R${:.2f}/mês'.format(p / pr))
    elif pr > 2 :
        print('20% de juros aplicado\nValor final: R${:.2f}/mês'.format(20 * (p / pr) / 100 + (p / pr)))
    else :
        print('Valor inválido')
