from random import randint, choice
print('=-' * 14)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=-' * 14)
vitorias = numero_jogador = 0
jogador = ''
PI = ('par', 'ímpar')
while True:
    numero_computador = randint(0, 10)
    computador = choice(('par', 'ímpar'))

    numero_jogador = int(input('Diga um valor: '))
    jogador = str(input('Par ou Ímpar? ')).strip().lower()
    while jogador not in PI:
        jogador = str(input('Par ou Ímpar? ')).strip().lower()

    print('--' * 14)

    soma = numero_computador + numero_jogador
    resultado = ''
    if soma % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'ímpar'

    decisao = ''
    if jogador == resultado:
        decisao = 'ganhou'
        vitorias += 1
        print(f'''Você jogou: {numero_jogador} 
computador jogou: {numero_computador}.
Total: {soma}
Resultado: {resultado}''')

        print('--' * 14)
        print('''VOCÊ GANHOU! 
VAMOS MAIS UMA VEZ...''')
        print('=-' * 14)

    else:
        decisao = 'perdeu'
        print(f'''Você jogou: {numero_jogador}
computador jogou: {numero_computador}. 
Total: {soma}
Resultado: {resultado}''')
        print('--' * 14)
        print('VOCÊ PERDEU!')
        print('--' * 14)
        break

print(f'Fim de jogo! Você teve {vitorias} vitórias.')
