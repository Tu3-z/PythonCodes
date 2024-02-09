dados = {}
dados['nome'] = str(input('Nome: '))
dados ['media'] = int(input(f'Média de {dados["nome"]}: '))
if dados['media'] < 6:
    dados['situacao'] = 'Reprovado'
else:
    dados['situacao'] = 'Aprovado'
print(f'Nome é igual a {dados["nome"]}')
print(f'Média igual a {dados["media"]}')
print(f'Situação é igual a {dados["situacao"]}')