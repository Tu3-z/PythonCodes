import random
om = [1, 2, 3]
print('1- Tesoura\n2- Pedra\n3- Papel')
e = int(input('Faça sua escolha: '))
em = random.choice(om)
if e == 1 and em == 3 :
    print('A máquina escolheu papel\nVocê ganhou!')
elif e == 1 and em == 2 :
    print ('A máquina escolheu pedra\nVocê perdeu!')
elif e == 1 and em == 1 :
    print('A máquina escolheu a mesma opção\nEmpate!')
    
elif e == 2 and em == 1 :
    print('A máquina escolheu tesoura\nVocê ganhou!')
elif e == 2 and em == 3 :
    print ('A máquina escolheu papel\nVocê perdeu!')
elif e == 2 and em == 2 :
    print('A máquina escolheu a mesma opção\nEmpate!')

elif e == 3 and em == 2 :
    print('A máquina escolheu pedra\nVocê ganhou!')
elif e == 3 and em == 1 :
    print ('A máquina escolheu tesoura\nVocê perdeu!')
elif e == 3 and em == 3 :
    print('A máquina escolheu a mesma opção\nEmpate!')
else : 
    print('Valor inválido')