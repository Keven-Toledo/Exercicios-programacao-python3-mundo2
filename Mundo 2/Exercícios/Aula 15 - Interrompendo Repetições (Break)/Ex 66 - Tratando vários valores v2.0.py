print('Atenção! o número 999 encerra o programa.')
soma = contagem = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    contagem += 1
print('=' * 25)
print(f'''Números contabilizados: {contagem} 
Soma Total: {soma}''')
