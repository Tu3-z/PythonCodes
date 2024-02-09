from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['ct'] = int(input('Carteira de trabalho (0 se não possuir): '))
dados['idade'] = datetime.now().year - dados['nascimento']
if dados['ct'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['aposentaria'] =  dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
    dados['salario'] = int(input('Salário: '))
    for k, v in dados.items():
        print(f'{k} tem valor {v}')
else:
    for k, v in dados.items():
        print(f'{k} tem valor {v}')
