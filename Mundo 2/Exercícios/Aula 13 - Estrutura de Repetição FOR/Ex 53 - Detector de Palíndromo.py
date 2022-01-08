frase = str(input('Digite um frase: ')).upper().strip()

separar_palavras = frase.split()
retirar_espacos = ''.join(separar_palavras)
inverter_frase = retirar_espacos[::-1]

print(f'O inverso de {retirar_espacos} é {inverter_frase}')
if retirar_espacos == inverter_frase:
    print('A frase digitada é um PALÍNDROMO.')
else:
    print('A frase digitada não é um PALÍNDROMO.')
