n1 = float(input('Primeira Nota: '))
n2 = float(input('Segundo nota: '))
media = (n1 + n2) / 2
print('Sua média final é {}.'.format(media))

if media < 5.0:
    situacao = 'Reprovado'
    print('Situação: {}{}{}.'.format('\033[31m', situacao, '\033[m'))
elif media < 7.0:
    situacao = 'Recuperação'
    print('Situação: {}{}{}'.format('\033[33m', situacao, '\033[m'))
elif media >= 7.0:
    situacao = 'Aprovado'
    print('Situação: {}{}{}'.format('\033[32m', situacao, '\033[m'))
