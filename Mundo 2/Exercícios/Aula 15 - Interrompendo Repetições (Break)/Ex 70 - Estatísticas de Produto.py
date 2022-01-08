contador = soma = contador_mil = caro = barato = 0
nome = ''
while True:
    print('=' * 25)
    contador += 1
    produto = str(input(f'Nome do {contador}º produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    soma += preco
    if preco > 1000:
        contador_mil += 1
    if contador == 1:
        barato = preco
        nome = produto
    else:
        if preco < barato:
            barato = preco
            nome = produto

    print('-' * 25)
    opcao = str(input('Deseja continuar? ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'''Total da compra: R$ {soma:.2f}
{contador_mil} produtos custam mais de R$ 1.000
Nome e preço do produto mais barato: {nome} custa R${barato} ''')
