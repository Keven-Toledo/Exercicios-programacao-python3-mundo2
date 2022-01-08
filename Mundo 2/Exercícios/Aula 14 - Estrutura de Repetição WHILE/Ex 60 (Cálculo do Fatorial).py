n = int(input('Escolha um número: '))
contador = n
fatorial = 1
while contador > 0:
    # print('{}'.format(contador), end='')
    # print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}! = {}'.format(n, fatorial))

'''n = int(input('Escolha um número: '))
mult = 1
for c in range(n, 0, -1):
    print(c, end='')
    mult *= c
print('{}! = {}'.format(n, mult))'''
