from time import sleep
numero = int(input('Digite um número: '))

vezes = 0
for ciclo in range(1, numero+1):
    if numero % ciclo == 0:
        print('\033[1;32m', end='')
        vezes += 1
    else:
        print('\033[1;31m', end='')
    print(ciclo, end='')
    sleep(1)

print(f'\n O número {numero} foi divisível {vezes} vezes.')
if vezes == 2:
    print(f'Por isso, o número {numero} é primo.')
else:
    print(f'Por isso, o número {numero} NÃO é primo.')
