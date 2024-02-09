lb = 'Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Athletico-PR', 'Atlético-MG', 'Santos', 'Fortaleza', 'Flamengo', 'São Paulo', 'Grêmio', 'Internacional', 'Bragantino', 'Bahia', 'Goiás', 'Vasco da Gama', 'Corinthians', 'Cuiabá', 'Coritiba', 'América-MG'
a = lb[:5]
b = lb[-4:]
c = sorted(lb)  
d = lb.index('Fortaleza')
print(f'5 primeiros: {a}\n4 últimos: {b}\nOrdem alfabética: {c}\nFortaleza esta na {d + 1}º posição')