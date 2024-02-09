from modulos import moeda2
num = int(input("Digite um número: R$"))
print(f"Metade: {moeda2.metade(num, True)}")
print(f"Dobro: {moeda2.dobro(num, True)}")
print(f"Aumentando 50%: {moeda2.aumentar(num, 50, True)}")
print(f"Diminuindo 25%: {moeda2.diminuir(num, 25, True)}")