from datetime import datetime

def voto(i):
    if i >= 18 and i <= 70:
        return 'OBRIGATÓRIO'
    elif i > 70 or i >= 16 and i <= 17:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


n = int(input('Ano de nascimento: '))
i = datetime.now().year - n
print(voto(i))
        
    