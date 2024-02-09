d = {}
l = []
g = []
go = []
o = 'S'
s = 0
while o == 'S':
    d['nome'] = str(input('Nome do jogador: '))
    d['partidas'] = int(input('Partidas jogadas: '))
    for c in range(0, d['partidas']):
        g.append(int(input(f'Gols na partida {c}: ')))
        s += g[c]
    go.append(g[:])
    d['gols'] = g[:]
    g.clear()
    d['total'] = s
    l.append(d.copy())
    o = str(input('Deseja continuar[S/N]: '))
print('Nome do jogador     Gols     Total')
for p, v in enumerate(l):
    print(f'{p} {v["nome"]}            {go[p]}     {v["total"]}')
op = int(input('Digite o número do jogador desejado para ver dados separados: '))
if op > len(l):
    op = input('Erro. Digito acima dos jogadores. Tente novamente: ')
while op != 999:
    print(f'Levantamento do jogador {l[op]["nome"]}')
    for i, g in enumerate(l[op]['gols']):
        print(f'      Na partida {i} fez {g}')
    op = int(input('Digite o número do jogador desejado para ver dados separados: '))
print('Programa encerrado')

        


   