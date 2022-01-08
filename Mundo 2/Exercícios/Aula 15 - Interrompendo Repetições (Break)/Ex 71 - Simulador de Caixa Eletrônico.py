print('=' * 30)
print('{:^30}'.format('BANCO TOLEDO'))
print('=' * 30)
valor = int(input('Valor para saque: R$'))
valor_total = valor
cedula = 50
contador_cedulas = 0
while True:
    if valor_total >= cedula:
        valor_total -= cedula
        contador_cedulas += 1
    else:
        if contador_cedulas != 0:
            print(f'{contador_cedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contador_cedulas = 0
        if valor_total == 0:
            break
