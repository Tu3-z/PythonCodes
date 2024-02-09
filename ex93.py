dados = {}
gols = []
dados['nome'] = str(input('Digite o nome do jogador: '))
p = int(input('Número de partidas jogadas: '))
s = 0
for c in range(0, p):
    gols.append(int(input(f'Gols da {c} partida: ')))
dados['gols'] = gols
t = 0
for s in gols:
    t += s
dados['total'] = t
print(dados)
print('='*40)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('='*40)
c = 0
print(f'O jogador {dados["nome"]} jogou {p} jogos')
for g in dados['gols']:
    print(f'    => Gols feitos na {c} partida: {g}')
    c += 1
print(f'Foi um total de {dados["total"]} gols')