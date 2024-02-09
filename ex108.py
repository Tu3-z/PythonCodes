from modulos import moeda
num = int(input("Digite um número: "))
print(f"Metade: {moeda.moeda(moeda.metade(num))}")
print(f"Dobro: {moeda.moeda(moeda.dobro(num))}")
print(f"Aumentando 50%: {moeda.moeda(moeda.aumentar(num, 50))}")
print(f"Diminuindo 25%: {moeda.moeda(moeda.diminuir(num, 25))}")