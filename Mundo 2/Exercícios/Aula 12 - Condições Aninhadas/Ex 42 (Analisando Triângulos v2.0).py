a = float(input('Termo a: '))
b = float(input('Termo b: '))
c = float(input('Termo c: '))

eixo_a = b + c
eixo_b = a + c
eixo_c = a + b

if a < eixo_a and b < eixo_b and c < eixo_c:
    print(f'Os lados ({a}/{b}/{c}) podem formar um triângulo.')

    if c == a == b:
        classi = 'Equilátero'
        print(f'''Todos os lados são iguais. 
Classificação (lados): {classi}''', end=' ')
    elif c != a == b or a != b == c or b != a == c:
        classi = 'Isosceles'
        print(f'''Há dois ângulos iguais e um diferente.
Classificação (lados): {classi}''', end=' ')
    elif a != b != c:
        classi = 'Escaleno'
        print(f'''Todos os lados são diferente.
Classificação (lados): {classi}''', end=' ')
else:
    print(f'Os lados ({a}/{b}/{c}) não podem formar um triângulo.')
