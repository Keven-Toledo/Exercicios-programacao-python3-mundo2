a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
contador = 1
while contador <= 10:
    an = a1 + (contador - 1) * r
    contador += 1
    print(an, end=' - ')
print('Fim')

# Laço do professor
'''termo = a1
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo += r
    cont += 1
print('Fim')'''
