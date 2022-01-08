print('=' * 60)
print('Visualize qualquer tabuada inserindo-na abaixo')
print('=' * 60)
while True:
    n = int(input('Quer ver qual tabuada?  '))
    print('-' * 20)
    if n <= 0:
        break
    for ciclo in range(1, 11):
        tabuada = n * ciclo
        print(f'{n} X {ciclo} = {tabuada}')
    print('-' * 20)
print('Programa Tabuada encerrado. Volte sempre!')
