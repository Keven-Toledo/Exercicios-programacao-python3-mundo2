termos = int(input('Quantos termos deseja ver: '))
T1 = 0
T2 = 1
print(f'{T1} - {T2} - ', end='')
contador = 3
while contador <= termos:
    T3 = T2 + T1
    T1 = T2
    T2 = T3
    print(f'{T3} - ', end='')
    contador += 1
print('FIM')
