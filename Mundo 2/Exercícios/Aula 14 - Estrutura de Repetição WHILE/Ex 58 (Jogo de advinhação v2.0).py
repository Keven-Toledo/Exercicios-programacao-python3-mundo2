from random import randint
computador = randint(0, 10)
print('='*60)
print('Desafio você advinhar o número que pensei entre 0 e 10!')
print('='*60)
usuario = int(input('Escolha um número: '))
palpites = 1
while usuario != computador:
    if usuario > computador:
        usuario = int(input('Menos... Tente mais uma vez: '))
        palpites += 1
    elif usuario < computador:
        usuario = int(input('Mais... Tente mais uma vez: '))
        palpites += 1
print('Você acertou! Foram necessários {} palpites. Meus parabéns!'.format(palpites))
