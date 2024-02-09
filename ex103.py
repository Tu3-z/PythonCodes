def ficha(n, g):
    if len(n) == 0:
        n = 'Desconhecido'
    if len(g) == 0:
        g = 0
    return print(f'O jogador {n} fez {g} gols')


n = str(input('Nome do jogador: '))
g = (input('Gols: '))
ficha(n, g)