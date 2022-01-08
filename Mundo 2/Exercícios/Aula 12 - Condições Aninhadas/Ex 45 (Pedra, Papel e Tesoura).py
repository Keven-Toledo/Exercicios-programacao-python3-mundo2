from random import choice
from time import sleep

x = 'Pedra'
y = 'Papel'
z = 'Tesoura'
pc = choice([x, y, z])

print('\033[1;31m''x='*20)
print('\033[1;33m''Vamos jogar Pedra, Papel ou Tesoura?')
print('\033[1;31m''x='*20)
us = str(input('\033[34m''Escolha: ''\033[m')).title()

print('\033[1;32m''PEEEDRA')
sleep(1)
print('\033[1;32m''PAPEEEEL')
sleep(1)
print('\033[1;32m''TESOUUU')
sleep(1)
print('\033[1;32m''RA!')

amarelo = '\033[1;33m'
verde = '\033[1;32m'
vermelho = '\033[1;31m'
limpa = '\033[m'
if pc != us:
    if us == 'Pedra':
        if pc == 'Tesoura':
            print(f'{verde}Você ganhou!{limpa} {vermelho}Escolhi {pc}.')
        else:
            print(f'{amarelo}Eu ganhei!!!{limpa} {vermelho}Escolhi {pc}.')
    elif us == 'Tesoura':
        if pc == 'Pedra':
            print(f'{amarelo}Eu ganhei!!!{limpa} {vermelho}Escolhi {pc}.')
        else:
            print(f'{verde}Você ganhou!{limpa} {vermelho}Escolhi {pc}.')
    elif us == 'Papel':
        if pc == 'Pedra':
            print(f'{verde}Você ganhou!{limpa} {vermelho}Escolhi {pc}.')
        else:
            print(f'{amarelo}Eu ganhei!!!{limpa} {vermelho}Escolhi {pc}.')
else:
    print('\033[1;33m''EMPATOU!!!')
