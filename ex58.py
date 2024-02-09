import random
c = 1
n = int(input('Digite o mesmo número que o computador escolheu 1 à 10: '))
np = random.randint(1, 10)
while n != np:
    n = int(input('Errado, digite outro número: '))
    c += 1
print('Parabéns! Você acetou com um total de {} tentativas\nO número escolhido foi {}'.format(c, np))
    