print('Calculadora de números inteiros e pares.')
soma = 0
cont_total = 0
cont_pares = 0
for contagem in range(1, 7):
    num = int(input(f'Digite o {contagem}º número: '))
    cont_total += 1
    if num % 2 == 0:
        cont_pares += 1
        soma = soma + num

if cont_pares == 1:
    print(f'''Você informou {cont_total} valores;
Sendo somente {cont_pares} par;
A soma vale: {soma}''')
else:
    print(f'''Você informou {cont_total} valores; 
Sendo que {cont_pares} são pares;
A soma vale: {soma}''')
