sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
# gen = ('M', 'F')
# while sexo not in gen:
while sexo not in 'MF':
    sexo = str(input('Valor inválido. Informe novamente seu sexo: ')).strip().upper()[0]
print('''Sexo: {} 
Situação: Liberado'''.format(sexo))
